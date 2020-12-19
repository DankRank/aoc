%{
#include <stdio.h>
int yylex();
#define yyerror(s) ((void)0)
%}
%start nterm0
%%
nterm90: nterm86 nterm86;
nterm122: nterm86 nterm1 | nterm99 nterm20;
nterm116: nterm86 nterm58 | nterm99 nterm75;
nterm20: nterm86 nterm123;
nterm62: nterm99 nterm95 | nterm86 nterm113;
nterm81: nterm76 nterm99 | nterm90 nterm86;
nterm106: nterm120 nterm86 | nterm93 nterm99;
nterm73: nterm99 nterm72 | nterm86 nterm45;
nterm117: nterm131 nterm99 | nterm72 nterm86;
nterm92: nterm86 nterm96 | nterm99 nterm98;
nterm13: nterm3 nterm99 | nterm118 nterm86;
nterm56: nterm90 nterm86 | nterm58 nterm99;
nterm85: nterm72 nterm99 | nterm51 nterm86;
nterm51: nterm99 nterm99 | nterm86 nterm86;
nterm59: nterm99 nterm25 | nterm86 nterm62;
nterm65: nterm99 nterm15 | nterm86 nterm97;
nterm112: nterm86 nterm13 | nterm99 nterm38;
nterm46: nterm33 nterm86 | nterm2 nterm99;
nterm10: nterm67 nterm86 | nterm68 nterm99;
nterm33: nterm120 nterm99 | nterm76 nterm86;
nterm38: nterm35 nterm86 | nterm125 nterm99;
nterm26: nterm86 nterm10 | nterm99 nterm55;
nterm1: nterm33 nterm99 | nterm60 nterm86;
nterm8: nterm42 | nterm42 nterm8;
nterm16: nterm51 nterm86 | nterm93 nterm99;
nterm107: nterm40 nterm99 | nterm2 nterm86;
nterm40: nterm17 nterm120;
nterm34: nterm86 nterm82 | nterm99 nterm127;
nterm88: nterm93 nterm17;
nterm2: nterm99 nterm51 | nterm86 nterm120;
nterm32: nterm100 nterm99 | nterm7 nterm86;
nterm113: nterm86 nterm127 | nterm99 nterm82;
nterm14: nterm73 nterm86 | nterm44 nterm99;
nterm25: nterm86 nterm101 | nterm99 nterm56;
nterm130: nterm110 nterm86 | nterm109 nterm99;
nterm19: nterm86 nterm4 | nterm99 nterm49;
nterm30: nterm86 nterm92 | nterm99 nterm70;
nterm27: nterm17 nterm86 | nterm86 nterm99;
nterm94: nterm47 nterm86 | nterm53 nterm99;
nterm115: nterm86 nterm107 | nterm99 nterm84;
nterm15: nterm76 nterm99 | nterm58 nterm86;
nterm58: nterm86 nterm99;
nterm105: nterm130 nterm86 | nterm32 nterm99;
nterm71: nterm120 nterm99 | nterm131 nterm86;
nterm12: nterm99 nterm131 | nterm86 nterm82;
nterm60: nterm72 nterm86 | nterm93 nterm99;
nterm84: nterm86 nterm102 | nterm99 nterm80;
nterm44: nterm99 nterm76 | nterm86 nterm72;
nterm125: nterm76 nterm99 | nterm131 nterm86;
nterm18: nterm99 nterm71 | nterm86 nterm52;
nterm129: nterm37 nterm86 | nterm111 nterm99;
nterm102: nterm99 nterm131 | nterm86 nterm76;
nterm66: nterm86 nterm105 | nterm99 nterm41;
nterm99: 'a';
nterm9: nterm99 nterm18 | nterm86 nterm65;
nterm131: nterm17 nterm99 | nterm99 nterm86;
nterm39: nterm76 nterm99 | nterm93 nterm86;
nterm64: nterm115 nterm99 | nterm114 nterm86;
nterm57: nterm86 nterm48 | nterm99 nterm94;
nterm35: nterm72 nterm86 | nterm51 nterm99;
nterm0: nterm8 nterm11;
nterm77: nterm86 nterm83 | nterm99 nterm106;
nterm118: nterm72 nterm86 | nterm75 nterm99;
nterm47: nterm99 nterm103 | nterm86 nterm85;
nterm23: nterm99 nterm27 | nterm86 nterm76;
nterm48: nterm119 nterm99 | nterm78 nterm86;
nterm49: nterm86 nterm51 | nterm99 nterm45;
nterm67: nterm86 nterm120;
nterm61: nterm86 nterm72 | nterm99 nterm127;
nterm108: nterm72 nterm99 | nterm72 nterm86;
nterm95: nterm86 nterm58 | nterm99 nterm90;
nterm83: nterm86 nterm27 | nterm99 nterm131;
nterm75: nterm86 nterm99 | nterm99 nterm99;
nterm101: nterm51 nterm99 | nterm27 nterm86;
nterm103: nterm90 nterm99 | nterm90 nterm86;
nterm128: nterm86 nterm69 | nterm99 nterm33;
nterm70: nterm99 nterm14 | nterm86 nterm19;
nterm52: nterm127 nterm86 | nterm90 nterm99;
nterm21: nterm86 nterm24 | nterm99 nterm59;
nterm22: nterm86 nterm63 | nterm99 nterm12;
nterm42: nterm79 nterm86 | nterm66 nterm99;
nterm97: nterm51 nterm17;
nterm104: nterm86 nterm33 | nterm99 nterm28;
nterm100: nterm99 nterm16 | nterm86 nterm39;
nterm72: nterm99 nterm86;
nterm78: nterm86 nterm43 | nterm99 nterm50;
nterm55: nterm86 nterm6 | nterm99 nterm34;
nterm45: nterm99 nterm99;
nterm5: nterm86 nterm46 | nterm99 nterm77;
nterm93: nterm99 nterm99 | nterm99 nterm86;
nterm6: nterm131 nterm99 | nterm51 nterm86;
nterm110: nterm71 nterm86 | nterm28 nterm99;
nterm68: nterm90 nterm86 | nterm27 nterm99;
nterm29: nterm87 nterm86 | nterm122 nterm99;
nterm80: nterm86 nterm93 | nterm99 nterm131;
nterm54: nterm120 nterm86 | nterm75 nterm99;
nterm43: nterm93 nterm86;
nterm98: nterm99 nterm103 | nterm86 nterm117;
nterm7: nterm101 nterm86 | nterm88 nterm99;
nterm127: nterm17 nterm86 | nterm99 nterm99;
nterm96: nterm86 nterm12 | nterm99 nterm61;
nterm41: nterm99 nterm5 | nterm86 nterm112;
nterm79: nterm86 nterm57 | nterm99 nterm21;
nterm11: nterm42 nterm31 | nterm42 nterm11 nterm31;
nterm86: 'b';
nterm111: nterm45 nterm99 | nterm72 nterm86;
nterm63: nterm76 nterm99 | nterm127 nterm86;
nterm124: nterm86 nterm81 | nterm99 nterm116;
nterm28: nterm86 nterm75 | nterm99 nterm58;
nterm82: nterm99 nterm86 | nterm86 nterm99;
nterm121: nterm64 nterm86 | nterm74 nterm99;
nterm87: nterm86 nterm124 | nterm99 nterm104;
nterm74: nterm99 nterm26 | nterm86 nterm9;
nterm31: nterm126 nterm99 | nterm121 nterm86;
nterm50: nterm99 nterm72;
nterm119: nterm34 nterm86 | nterm36 nterm99;
nterm36: nterm86 nterm82 | nterm99 nterm75;
nterm91: nterm86 nterm131;
nterm3: nterm58 nterm99 | nterm27 nterm86;
nterm114: nterm99 nterm129 | nterm86 nterm22;
nterm24: nterm86 nterm89 | nterm99 nterm128;
nterm53: nterm91 nterm99 | nterm95 nterm86;
nterm126: nterm29 nterm86 | nterm30 nterm99;
nterm109: nterm99 nterm108 | nterm86 nterm23;
nterm17: nterm86 | nterm99;
nterm76: nterm86 nterm86 | nterm99 nterm86;
nterm120: nterm17 nterm17;
nterm89: nterm54 nterm86 | nterm37 nterm99;
nterm4: nterm99 nterm131 | nterm86 nterm58;
nterm69: nterm27 nterm17;
nterm37: nterm99 nterm58;
nterm123: nterm86 nterm76 | nterm99 nterm82;
%%
const char *lex_input = NULL;
int yylex()
{
	if (*lex_input == '\0' || *lex_input == '\n')
		return YYEOF;
	return *lex_input++;
}
int main()
{
	char buf[512];
	int total = 0;
	while (fgets(buf,512,stdin)) {
		lex_input = buf;
		if (!yyparse())
			total++;
	}
	printf("%d\n", total);
}
