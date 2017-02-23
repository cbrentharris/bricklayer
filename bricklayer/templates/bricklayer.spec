(* ============================================================================================== *)
datatype lexresult  = SHELL of string * string * {line: word, column: word};
val error           = fn x => TextIO.output(TextIO.stdOut,x ^ "\n")
val eof             = fn () => SHELL("","eof",getNextTokenPos(""))
val counter         = ref 0;
(* ============================================================================================== *)
(* ------------------------------------------------------------------ *)
(* assumes that ">" does not occur as part of a nonterminal symbol *)
fun generateSchemaTokenName( yytext ) =
    let
        fun split(x, []   ) =  raise General.Fail("an_error")
          | split(x, y::ys) = if x=y then ys else split(x,ys);

        fun splitFirst(symbol,[])    =     [] (* symbol was not in the input list *)
          | splitFirst(symbol,x::xs) =     if x = symbol
                        then (* found split point *)
                            []
                        else (* keep looking      *)
                            x::splitFirst(symbol,xs);

        val s0   = explode(yytext);
        val s1   = split(#"<",s0);
        val s2   = splitFirst(#">",s1);
    in
        implode(explode("!#schema_variable_") @ s2)
    end;

(* ------------------------------------------------------------------ *)

(* ============================================================================================== *)
%%
%header (functor Target_LexFn(val getNextTokenPos : string -> {line: word, column: word}));

digit        = [0-9];
integer      = "~"? {digit}+;
lowerAlpha   = [a-z];
upperAlpha   = [A-Z];
alpha        = [A-Za-z];
alphanumeric = [A-Za-z0-9'_];

equalSymbol  = "=";
bangSymbol   = "!";
ltSymbol     = "<";
gtSymbol     = ">";
negSymbol    = "~";
hashSymbol   = "#";
dollarSymbol = "$";

funkySymbol  = ( {equalSymbol} | {bangSymbol} | {ltSymbol} | {gtSymbol} | {negSymbol} | {hashSymbol} | {dollarSymbol} );

funkyId          = {funkySymbol}{funkySymbol}+ | {dollarSymbol} ;
basic_id         = {alpha}{alphanumeric}*;
type_variable    = "'"+  {basic_id};
eqtype_variable  = "\""+ {basic_id};

real_1           = {digit}+ "." {digit}+ ;
real_2           = {digit}+ ("e" | "E") "~"? {digit}+;
real_3           = {digit}+ "." {digit}+ ("e" | "E") "~"? {digit}+;
real             = {real_1} | {real_2} | {real_3};

hexadecimal      = ([A-F] | [a-f] | {digit});
word_value       = ( "0w" {digit}+ | "0wx" {hexadecimal}+ );
boolean_value    = "true" | "false";

schema_id    = "<" {alpha}{alphanumeric}* ">_" {alphanumeric}+;

character    = "#""\"" ([^\"\\] | \\. ) "\"";
ws           = [\  \t \n];

nl           = [\n];
comment      = "%" ([^*\n] .* | {nl});

singleLineStringGuts = ([^\"\\] | \\. )*;
multilineStringGuts  = {singleLineStringGuts} ("\\" {ws}+ ( "\\" {singleLineStringGuts} "\\" {ws}+ )* "\\" {singleLineStringGuts})?;
string               = "\"" {multilineStringGuts} "\"";

%s COMMENT;
%%

<COMMENT> "(*"              => ( counter := !counter + 1; getNextTokenPos(yytext); lex()         );
<COMMENT> "*)"              => ( counter := !counter - 1;
                                 if !counter = 0 then YYBEGIN INITIAL
                                 else ();
                                 getNextTokenPos(yytext); lex()                                  );
<COMMENT> .                 => ( getNextTokenPos(yytext); lex()                                  );
<COMMENT> {ws}+             => ( getNextTokenPos(yytext); lex()  );

<INITIAL> "(*"              => ( YYBEGIN COMMENT;
                                 counter := !counter + 1;
                                 getNextTokenPos(yytext); lex()                                  );


<INITIAL> "#"                       => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> ";"                       => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> ":"                       => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> ":>"                      => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "::"                      => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> ","                       => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "."                       => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "..."                     => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "@"                       => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "|"                       => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "("                       => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> ")"                       => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "["                       => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "]"                       => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "{"                       => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "}"                       => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> ":="                      => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "="                       => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "<>"                      => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "<"                       => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "<="                      => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> ">"                       => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> ">="                      => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "=>"                      => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "->"                      => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "+"                       => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "-"                       => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "^"                       => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "*"                       => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "_"                       => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "/"                       => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "?"                       => ( SHELL("basic_id"                        , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "!"                       => ( SHELL("basic_id"                        , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "~"                       => ( SHELL("basic_id"                        , yytext,     getNextTokenPos(yytext))    );

<INITIAL> "abstype"                 => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "and"                     => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "andalso"                 => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "as"                      => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "case"                    => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "datatype"                => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "def"                     => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "div"                     => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "do"                      => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "else"                    => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "end"                     => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "exception"               => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "fn"                      => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "fun"                     => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "functor"                 => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "handle"                  => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "if"                      => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "in"                      => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "include"                 => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "import"                  => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "infix"                   => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "infixr"                  => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "nonfix"                  => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "let"                     => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "local"                   => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "o"                       => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "of"                      => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "open"                    => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "op"                      => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "orelse"                  => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "mod"                     => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "NONE"                    => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "raise"                   => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "rec"                     => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "ref"                     => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "sharing"                 => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "sig"                     => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "signature"               => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "struct"                  => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "structure"               => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "SOME"                    => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "then"                    => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "type"                    => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "val"                     => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "where"                   => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "while"                   => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "with"                    => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );
<INITIAL> "withtype"                => ( SHELL(yytext                            , yytext,     getNextTokenPos(yytext))    );

<INITIAL> {integer}                 => ( SHELL("integer_value"                   , yytext,     getNextTokenPos(yytext))    );
<INITIAL> {real}                    => ( SHELL("real_value"                      , yytext,     getNextTokenPos(yytext))    );
<INITIAL> {boolean_value}           => ( SHELL("boolean_value"                   , yytext,     getNextTokenPos(yytext))    );
<INITIAL> {type_variable}           => ( SHELL("type_variable"                   , yytext,     getNextTokenPos(yytext))    );
<INITIAL> {eqtype_variable}         => ( SHELL("eqtype_variable"                 , yytext,     getNextTokenPos(yytext))    );
<INITIAL> {basic_id}                => ( SHELL("basic_id"                        , yytext,     getNextTokenPos(yytext))    );
<INITIAL> {funkyId}                 => ( SHELL("basic_id"                        , yytext,     getNextTokenPos(yytext))    );

<INITIAL> {character}               => ( SHELL("char_value"                      , yytext, getNextTokenPos yytext) );
<INITIAL> {string}                  => ( SHELL("string_value"                    , yytext, getNextTokenPos yytext) );
<INITIAL> {word_value}              => ( SHELL("word_value"                      , yytext,     getNextTokenPos(yytext))    );

<INITIAL> {comment}                 => ( getNextTokenPos(yytext); lex()  );
<INITIAL> {ws}+                     => ( getNextTokenPos(yytext); lex()  );

<INITIAL> {schema_id}               => ( SHELL(generateSchemaTokenName(yytext), yytext, getNextTokenPos(yytext))    );
<INITIAL> "[:]"                     => ( SHELL(""        , yytext, getNextTokenPos(yytext))    );

