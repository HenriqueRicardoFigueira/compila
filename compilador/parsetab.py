
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftSENAOleftIGUALMAIORIGUALMAIORMENORIGUALMENORleftADICAOSUBTRACAOleftMULTIPLICACAODIVISAOABRE_COL ABRE_PAR ADICAO ATE ATRIBUICAO CIENTIFICO DIFERENTE DIVISAO DOIS_PONTOS ENTAO ESCREVA E_LOGI FECHA_COL FECHA_PAR FIM FLUTUANTE ID IGUAL INTEIRO LEIA MAIOR MAIORIGUAL MAIS MENOR MENORIGUAL MENOS MULTIPLICACAO NEGACAO OU_LOGI REPITA RETORNA SE SENAO SUBTRACAO VIRGULAprograma : lista_declaracoeslista_declaracoes : lista_declaracoes declaracaolista_declaracoes : declaracao\n\t    \tdeclaracao \t: declaracao_variaveis\n\t    \t\t\t\t| inicializacao_variaveis\n\t    \t\t\t\t| declaracao_funcao\n\t    declaracao_variaveis : tipo DOIS_PONTOS lista_variaveisinicializacao_variaveis : atribuicaolista_variaveis : lista_variaveis VIRGULA varlista_variaveis : varvar : IDvar : ID indiceindice : indice ABRE_COL expressao FECHA_COLindice : ABRE_COL expressao FECHA_COLtipo : INTEIROtipo : FLUTUANTEtipo : CIENTIFICOdeclaracao_funcao : tipo cabecalhodeclaracao_funcao : cabecalhocabecalho : ID ABRE_PAR lista_parametros FECHA_PAR corpo FIMlista_parametros : lista_parametros VIRGULA parametro\n    \t\t\tlista_parametros \t: parametro\n    \t\t\t\t\t\t\t\t| vazio\n    \tparametro : tipo DOIS_PONTOS IDparametro : parametro ABRE_COL FECHA_COLcorpo \t: corpo acaocorpo : vazio\n    \t\tacao \t: expressao\n    \t\t\t\t| declaracao_variaveis\n    \t\t\t\t| se\n    \t\t\t\t| repita\n    \t\t\t\t| leia\n    \t\t\t\t| escreva\n    \t\t\t\t| retorna\n    \t\t\t\t| error\n    \tse : SE expressao ENTAO corpo FIMse : SE expressao ENTAO corpo SENAO corpo FIMrepita : REPITA corpo ATE expressaoatribuicao : var ATRIBUICAO expressaoleia : LEIA ABRE_PAR ID FECHA_PARescreva : ESCREVA ABRE_PAR expressao FECHA_PARretorna : RETORNA ABRE_PAR expressao FECHA_PAR\n    \t\texpressao \t: expressao_simples\n    \t\t\t\t\t| atribuicao \n    \texpressao_simples : expressao_aditivaexpressao_simples : expressao_simples operador_relacional expressao_aditivaexpressao_aditiva : expressao_multiplicativaexpressao_aditiva : expressao_aditiva operador_soma expressao_multiplicativaexpressao_multiplicativa : expressao_unariaexpressao_multiplicativa : expressao_multiplicativa operador_multiplicacao expressao_unariaexpressao_unaria : fatorexpressao_unaria : operador_soma fator\t\n    \t\toperador_relacional \t: MENOR\n    \t\t\t\t\t\t\t\t| MAIOR\n    \t\t\t\t\t\t\t\t| IGUAL\n    \t\t\t\t\t\t\t\t| DIFERENTE\n    \t\t\t\t\t\t\t\t| MENORIGUAL \n    \t\t\t\t\t\t\t\t| MAIORIGUAL\n    \t\t\t\t\t\t\t\t| E_LOGI\n    \t\t\t\t\t\t\t\t| NEGACAO\n    \t\n    \t\toperador_soma \t: ADICAO\n    \t\t\t\t\t\t| SUBTRACAO\n    \t\n    \t\toperador_multiplicacao \t: MULTIPLICACAO\n    \t\t\t\t\t\t\t\t| DIVISAO\n    \tinteiro : INTEIROflutuante : FLUTUANTE\t\n    \t\tfator \t: var\n    \t\t\t\t| chamada_funcao\n    \t\t\t\t| inteiro\n                    | flutuante\n    \tfator : ABRE_PAR expressao FECHA_PARchamada_funcao : ID ABRE_PAR lista_argumentos FECHA_PARlista_argumentos \t: lista_argumentos VIRGULA expressao\n    \t\tlista_argumentos \t: expressao\n    \t\t\t\t\t\t\t| vazio\n    \tvazio :'
    
_lr_action_items = {'INTEIRO':([0,2,3,4,5,6,8,9,15,17,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,48,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,73,74,75,76,77,81,82,83,87,88,89,90,91,92,93,94,95,96,97,98,99,101,102,106,107,110,112,113,114,115,119,120,121,122,123,124,125,126,127,],[10,10,-3,-4,-5,-6,-8,-19,-2,-18,42,10,-12,42,-7,-10,-11,-67,-39,-43,-44,-45,-47,42,-11,-49,-51,-68,-69,-70,42,-61,-62,-65,-66,42,42,-53,-54,-55,-56,-57,-58,-59,-60,42,42,-63,-64,-52,-67,42,-76,10,-14,-9,-46,-48,-50,-71,106,-27,-13,-72,42,-20,-26,-28,-29,-30,-31,-32,-33,-34,-35,42,-76,-65,-66,106,42,42,-76,42,106,-38,-40,-41,-42,-36,-76,106,-37,]),'FLUTUANTE':([0,2,3,4,5,6,8,9,15,17,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,48,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,73,74,75,76,77,81,82,83,87,88,89,90,91,92,93,94,95,96,97,98,99,101,102,106,107,110,112,113,114,115,119,120,121,122,123,124,125,126,127,],[11,11,-3,-4,-5,-6,-8,-19,-2,-18,43,11,-12,43,-7,-10,-11,-67,-39,-43,-44,-45,-47,43,-11,-49,-51,-68,-69,-70,43,-61,-62,-65,-66,43,43,-53,-54,-55,-56,-57,-58,-59,-60,43,43,-63,-64,-52,-67,43,-76,11,-14,-9,-46,-48,-50,-71,107,-27,-13,-72,43,-20,-26,-28,-29,-30,-31,-32,-33,-34,-35,43,-76,-65,-66,107,43,43,-76,43,107,-38,-40,-41,-42,-36,-76,107,-37,]),'CIENTIFICO':([0,2,3,4,5,6,8,9,15,17,20,21,23,24,25,26,27,28,29,30,31,33,34,35,36,37,38,42,43,64,65,68,69,73,74,75,76,77,81,82,83,87,88,90,91,92,93,94,95,96,97,98,99,102,106,107,110,114,119,120,121,122,123,124,125,126,127,],[12,12,-3,-4,-5,-6,-8,-19,-2,-18,12,-12,-7,-10,-11,-67,-39,-43,-44,-45,-47,-11,-49,-51,-68,-69,-70,-65,-66,-52,-67,-76,12,-14,-9,-46,-48,-50,-71,12,-27,-13,-72,-20,-26,-28,-29,-30,-31,-32,-33,-34,-35,-76,-65,-66,12,-76,12,-38,-40,-41,-42,-36,-76,12,-37,]),'ID':([0,2,3,4,5,6,7,8,9,10,11,12,15,16,17,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,71,73,74,75,76,77,81,82,83,87,88,89,90,91,92,93,94,95,96,97,98,99,101,102,106,107,110,111,112,113,114,115,119,120,121,122,123,124,125,126,127,],[14,14,-3,-4,-5,-6,18,-8,-19,-15,-16,-17,-2,25,-18,33,-12,33,-7,-10,-11,-67,-39,-43,-44,-45,-47,33,-11,-49,-51,-68,-69,-70,33,-61,-62,-65,-66,33,25,33,-53,-54,-55,-56,-57,-58,-59,-60,33,33,-63,-64,-52,-67,33,-76,86,-14,-9,-46,-48,-50,-71,33,-27,-13,-72,33,-20,-26,-28,-29,-30,-31,-32,-33,-34,-35,33,-76,-65,-66,33,116,33,33,-76,33,33,-38,-40,-41,-42,-36,-76,33,-37,]),'$end':([1,2,3,4,5,6,8,9,15,17,21,23,24,25,26,27,28,29,30,31,33,34,35,36,37,38,42,43,64,65,73,74,75,76,77,81,87,88,90,],[0,-1,-3,-4,-5,-6,-8,-19,-2,-18,-12,-7,-10,-11,-67,-39,-43,-44,-45,-47,-11,-49,-51,-68,-69,-70,-65,-66,-52,-67,-14,-9,-46,-48,-50,-71,-13,-72,-20,]),'DOIS_PONTOS':([7,10,11,12,47,100,106,107,],[16,-15,-16,-17,71,16,-15,-16,]),'ATRIBUICAO':([13,14,21,26,33,73,87,],[19,-11,-12,19,-11,-14,-13,]),'ABRE_PAR':([14,18,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,48,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,73,74,75,76,77,81,82,83,87,88,89,91,92,93,94,95,96,97,98,99,101,102,103,104,105,106,107,110,112,113,114,115,119,120,121,122,123,124,125,126,127,],[20,20,39,-12,39,-7,-10,-11,-67,-39,-43,-44,-45,-47,39,66,-49,-51,-68,-69,-70,39,-61,-62,-65,-66,39,39,-53,-54,-55,-56,-57,-58,-59,-60,39,39,-63,-64,-52,-67,39,-76,-14,-9,-46,-48,-50,-71,39,-27,-13,-72,39,-26,-28,-29,-30,-31,-32,-33,-34,-35,39,-76,111,112,113,-65,-66,39,39,39,-76,39,39,-38,-40,-41,-42,-36,-76,39,-37,]),'ABRE_COL':([14,21,25,33,45,73,84,85,86,87,],[22,48,22,22,70,-14,70,-25,-24,-13,]),'ADICAO':([19,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,37,38,39,40,41,42,43,48,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,73,74,75,76,77,81,82,83,87,88,89,91,92,93,94,95,96,97,98,99,101,102,106,107,110,112,113,114,115,119,120,121,122,123,124,125,126,127,],[40,-12,40,-7,-10,-11,-67,-39,-43,-44,40,-47,-11,-49,-51,-68,-69,-70,40,-61,-62,-65,-66,40,40,-53,-54,-55,-56,-57,-58,-59,-60,40,40,-63,-64,-52,-67,40,-76,-14,-9,40,-48,-50,-71,40,-27,-13,-72,40,-26,-28,-29,-30,-31,-32,-33,-34,-35,40,-76,-65,-66,40,40,40,-76,40,40,-38,-40,-41,-42,-36,-76,40,-37,]),'SUBTRACAO':([19,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,37,38,39,40,41,42,43,48,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,73,74,75,76,77,81,82,83,87,88,89,91,92,93,94,95,96,97,98,99,101,102,106,107,110,112,113,114,115,119,120,121,122,123,124,125,126,127,],[41,-12,41,-7,-10,-11,-67,-39,-43,-44,41,-47,-11,-49,-51,-68,-69,-70,41,-61,-62,-65,-66,41,41,-53,-54,-55,-56,-57,-58,-59,-60,41,41,-63,-64,-52,-67,41,-76,-14,-9,41,-48,-50,-71,41,-27,-13,-72,41,-26,-28,-29,-30,-31,-32,-33,-34,-35,41,-76,-65,-66,41,41,41,-76,41,41,-38,-40,-41,-42,-36,-76,41,-37,]),'FECHA_PAR':([20,21,26,27,28,29,30,31,33,34,35,36,37,38,42,43,44,45,46,64,65,66,67,73,75,76,77,78,79,80,81,84,85,86,87,88,108,116,117,118,],[-76,-12,-67,-39,-43,-44,-45,-47,-11,-49,-51,-68,-69,-70,-65,-66,68,-22,-23,-52,-67,-76,81,-14,-46,-48,-50,88,-74,-75,-71,-21,-25,-24,-13,-72,-73,121,122,123,]),'VIRGULA':([20,21,23,24,25,26,27,28,29,30,31,33,34,35,36,37,38,42,43,44,45,46,64,65,66,73,74,75,76,77,78,79,80,81,84,85,86,87,88,108,],[-76,-12,50,-10,-11,-67,-39,-43,-44,-45,-47,-11,-49,-51,-68,-69,-70,-65,-66,69,-22,-23,-52,-67,-76,-14,-9,-46,-48,-50,89,-74,-75,-71,-21,-25,-24,-13,-72,-73,]),'FIM':([21,23,24,25,26,27,28,29,30,31,33,34,35,36,37,38,42,43,64,65,68,73,74,75,76,77,81,82,83,87,88,91,92,93,94,95,96,97,98,99,106,107,114,119,120,121,122,123,124,125,126,127,],[-12,-7,-10,-11,-67,-39,-43,-44,-45,-47,-11,-49,-51,-68,-69,-70,-65,-66,-52,-67,-76,-14,-9,-46,-48,-50,-71,90,-27,-13,-72,-26,-28,-29,-30,-31,-32,-33,-34,-35,-65,-66,-76,124,-38,-40,-41,-42,-36,-76,127,-37,]),'error':([21,23,24,25,26,27,28,29,30,31,33,34,35,36,37,38,42,43,64,65,68,73,74,75,76,77,81,82,83,87,88,91,92,93,94,95,96,97,98,99,102,106,107,110,114,119,120,121,122,123,124,125,126,127,],[-12,-7,-10,-11,-67,-39,-43,-44,-45,-47,-11,-49,-51,-68,-69,-70,-65,-66,-52,-67,-76,-14,-9,-46,-48,-50,-71,99,-27,-13,-72,-26,-28,-29,-30,-31,-32,-33,-34,-35,-76,-65,-66,99,-76,99,-38,-40,-41,-42,-36,-76,99,-37,]),'SE':([21,23,24,25,26,27,28,29,30,31,33,34,35,36,37,38,42,43,64,65,68,73,74,75,76,77,81,82,83,87,88,91,92,93,94,95,96,97,98,99,102,106,107,110,114,119,120,121,122,123,124,125,126,127,],[-12,-7,-10,-11,-67,-39,-43,-44,-45,-47,-11,-49,-51,-68,-69,-70,-65,-66,-52,-67,-76,-14,-9,-46,-48,-50,-71,101,-27,-13,-72,-26,-28,-29,-30,-31,-32,-33,-34,-35,-76,-65,-66,101,-76,101,-38,-40,-41,-42,-36,-76,101,-37,]),'REPITA':([21,23,24,25,26,27,28,29,30,31,33,34,35,36,37,38,42,43,64,65,68,73,74,75,76,77,81,82,83,87,88,91,92,93,94,95,96,97,98,99,102,106,107,110,114,119,120,121,122,123,124,125,126,127,],[-12,-7,-10,-11,-67,-39,-43,-44,-45,-47,-11,-49,-51,-68,-69,-70,-65,-66,-52,-67,-76,-14,-9,-46,-48,-50,-71,102,-27,-13,-72,-26,-28,-29,-30,-31,-32,-33,-34,-35,-76,-65,-66,102,-76,102,-38,-40,-41,-42,-36,-76,102,-37,]),'LEIA':([21,23,24,25,26,27,28,29,30,31,33,34,35,36,37,38,42,43,64,65,68,73,74,75,76,77,81,82,83,87,88,91,92,93,94,95,96,97,98,99,102,106,107,110,114,119,120,121,122,123,124,125,126,127,],[-12,-7,-10,-11,-67,-39,-43,-44,-45,-47,-11,-49,-51,-68,-69,-70,-65,-66,-52,-67,-76,-14,-9,-46,-48,-50,-71,103,-27,-13,-72,-26,-28,-29,-30,-31,-32,-33,-34,-35,-76,-65,-66,103,-76,103,-38,-40,-41,-42,-36,-76,103,-37,]),'ESCREVA':([21,23,24,25,26,27,28,29,30,31,33,34,35,36,37,38,42,43,64,65,68,73,74,75,76,77,81,82,83,87,88,91,92,93,94,95,96,97,98,99,102,106,107,110,114,119,120,121,122,123,124,125,126,127,],[-12,-7,-10,-11,-67,-39,-43,-44,-45,-47,-11,-49,-51,-68,-69,-70,-65,-66,-52,-67,-76,-14,-9,-46,-48,-50,-71,104,-27,-13,-72,-26,-28,-29,-30,-31,-32,-33,-34,-35,-76,-65,-66,104,-76,104,-38,-40,-41,-42,-36,-76,104,-37,]),'RETORNA':([21,23,24,25,26,27,28,29,30,31,33,34,35,36,37,38,42,43,64,65,68,73,74,75,76,77,81,82,83,87,88,91,92,93,94,95,96,97,98,99,102,106,107,110,114,119,120,121,122,123,124,125,126,127,],[-12,-7,-10,-11,-67,-39,-43,-44,-45,-47,-11,-49,-51,-68,-69,-70,-65,-66,-52,-67,-76,-14,-9,-46,-48,-50,-71,105,-27,-13,-72,-26,-28,-29,-30,-31,-32,-33,-34,-35,-76,-65,-66,105,-76,105,-38,-40,-41,-42,-36,-76,105,-37,]),'ATE':([21,23,24,25,26,27,28,29,30,31,33,34,35,36,37,38,42,43,64,65,73,74,75,76,77,81,83,87,88,91,92,93,94,95,96,97,98,99,102,106,107,110,120,121,122,123,124,127,],[-12,-7,-10,-11,-67,-39,-43,-44,-45,-47,-11,-49,-51,-68,-69,-70,-65,-66,-52,-67,-14,-9,-46,-48,-50,-71,-27,-13,-72,-26,-28,-29,-30,-31,-32,-33,-34,-35,-76,-65,-66,115,-38,-40,-41,-42,-36,-37,]),'SENAO':([21,23,24,25,26,27,28,29,30,31,33,34,35,36,37,38,42,43,64,65,73,74,75,76,77,81,83,87,88,91,92,93,94,95,96,97,98,99,106,107,114,119,120,121,122,123,124,127,],[-12,-7,-10,-11,-67,-39,-43,-44,-45,-47,-11,-49,-51,-68,-69,-70,-65,-66,-52,-67,-14,-9,-46,-48,-50,-71,-27,-13,-72,-26,-28,-29,-30,-31,-32,-33,-34,-35,-65,-66,-76,125,-38,-40,-41,-42,-36,-37,]),'MULTIPLICACAO':([21,26,31,33,34,35,36,37,38,42,43,64,65,73,76,77,81,87,88,106,107,],[-12,-67,62,-11,-49,-51,-68,-69,-70,-65,-66,-52,-67,-14,62,-50,-71,-13,-72,-65,-66,]),'DIVISAO':([21,26,31,33,34,35,36,37,38,42,43,64,65,73,76,77,81,87,88,106,107,],[-12,-67,63,-11,-49,-51,-68,-69,-70,-65,-66,-52,-67,-14,63,-50,-71,-13,-72,-65,-66,]),'MENOR':([21,26,28,30,31,33,34,35,36,37,38,42,43,64,65,73,75,76,77,81,87,88,106,107,],[-12,-67,52,-45,-47,-11,-49,-51,-68,-69,-70,-65,-66,-52,-67,-14,-46,-48,-50,-71,-13,-72,-65,-66,]),'MAIOR':([21,26,28,30,31,33,34,35,36,37,38,42,43,64,65,73,75,76,77,81,87,88,106,107,],[-12,-67,53,-45,-47,-11,-49,-51,-68,-69,-70,-65,-66,-52,-67,-14,-46,-48,-50,-71,-13,-72,-65,-66,]),'IGUAL':([21,26,28,30,31,33,34,35,36,37,38,42,43,64,65,73,75,76,77,81,87,88,106,107,],[-12,-67,54,-45,-47,-11,-49,-51,-68,-69,-70,-65,-66,-52,-67,-14,-46,-48,-50,-71,-13,-72,-65,-66,]),'DIFERENTE':([21,26,28,30,31,33,34,35,36,37,38,42,43,64,65,73,75,76,77,81,87,88,106,107,],[-12,-67,55,-45,-47,-11,-49,-51,-68,-69,-70,-65,-66,-52,-67,-14,-46,-48,-50,-71,-13,-72,-65,-66,]),'MENORIGUAL':([21,26,28,30,31,33,34,35,36,37,38,42,43,64,65,73,75,76,77,81,87,88,106,107,],[-12,-67,56,-45,-47,-11,-49,-51,-68,-69,-70,-65,-66,-52,-67,-14,-46,-48,-50,-71,-13,-72,-65,-66,]),'MAIORIGUAL':([21,26,28,30,31,33,34,35,36,37,38,42,43,64,65,73,75,76,77,81,87,88,106,107,],[-12,-67,57,-45,-47,-11,-49,-51,-68,-69,-70,-65,-66,-52,-67,-14,-46,-48,-50,-71,-13,-72,-65,-66,]),'E_LOGI':([21,26,28,30,31,33,34,35,36,37,38,42,43,64,65,73,75,76,77,81,87,88,106,107,],[-12,-67,58,-45,-47,-11,-49,-51,-68,-69,-70,-65,-66,-52,-67,-14,-46,-48,-50,-71,-13,-72,-65,-66,]),'NEGACAO':([21,26,28,30,31,33,34,35,36,37,38,42,43,64,65,73,75,76,77,81,87,88,106,107,],[-12,-67,59,-45,-47,-11,-49,-51,-68,-69,-70,-65,-66,-52,-67,-14,-46,-48,-50,-71,-13,-72,-65,-66,]),'FECHA_COL':([21,26,27,28,29,30,31,33,34,35,36,37,38,42,43,49,64,65,70,72,73,75,76,77,81,87,88,],[-12,-67,-39,-43,-44,-45,-47,-11,-49,-51,-68,-69,-70,-65,-66,73,-52,-67,85,87,-14,-46,-48,-50,-71,-13,-72,]),'ENTAO':([21,26,27,28,29,30,31,33,34,35,36,37,38,42,43,64,65,73,75,76,77,81,87,88,109,],[-12,-67,-39,-43,-44,-45,-47,-11,-49,-51,-68,-69,-70,-65,-66,-52,-67,-14,-46,-48,-50,-71,-13,-72,114,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'lista_declaracoes':([0,],[2,]),'declaracao':([0,2,],[3,15,]),'declaracao_variaveis':([0,2,82,110,119,126,],[4,4,93,93,93,93,]),'inicializacao_variaveis':([0,2,],[5,5,]),'declaracao_funcao':([0,2,],[6,6,]),'tipo':([0,2,20,69,82,110,119,126,],[7,7,47,47,100,100,100,100,]),'atribuicao':([0,2,19,22,39,48,66,82,89,101,110,112,113,115,119,126,],[8,8,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'cabecalho':([0,2,7,],[9,9,17,]),'var':([0,2,16,19,22,32,39,48,50,51,60,61,66,82,89,101,110,112,113,115,119,126,],[13,13,24,26,26,65,26,26,74,65,65,65,26,26,26,26,26,26,26,26,26,26,]),'indice':([14,25,33,],[21,21,21,]),'lista_variaveis':([16,],[23,]),'expressao':([19,22,39,48,66,82,89,101,110,112,113,115,119,126,],[27,49,67,72,79,92,108,109,92,117,118,120,92,92,]),'expressao_simples':([19,22,39,48,66,82,89,101,110,112,113,115,119,126,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'expressao_aditiva':([19,22,39,48,51,66,82,89,101,110,112,113,115,119,126,],[30,30,30,30,75,30,30,30,30,30,30,30,30,30,30,]),'expressao_multiplicativa':([19,22,39,48,51,60,66,82,89,101,110,112,113,115,119,126,],[31,31,31,31,31,76,31,31,31,31,31,31,31,31,31,31,]),'operador_soma':([19,22,30,39,48,51,60,61,66,75,82,89,101,110,112,113,115,119,126,],[32,32,60,32,32,32,32,32,32,60,32,32,32,32,32,32,32,32,32,]),'expressao_unaria':([19,22,39,48,51,60,61,66,82,89,101,110,112,113,115,119,126,],[34,34,34,34,34,34,77,34,34,34,34,34,34,34,34,34,34,]),'fator':([19,22,32,39,48,51,60,61,66,82,89,101,110,112,113,115,119,126,],[35,35,64,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'chamada_funcao':([19,22,32,39,48,51,60,61,66,82,89,101,110,112,113,115,119,126,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'inteiro':([19,22,32,39,48,51,60,61,66,82,89,101,110,112,113,115,119,126,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'flutuante':([19,22,32,39,48,51,60,61,66,82,89,101,110,112,113,115,119,126,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'lista_parametros':([20,],[44,]),'parametro':([20,69,],[45,84,]),'vazio':([20,66,68,102,114,125,],[46,80,83,83,83,83,]),'operador_relacional':([28,],[51,]),'operador_multiplicacao':([31,76,],[61,61,]),'lista_argumentos':([66,],[78,]),'corpo':([68,102,114,125,],[82,110,119,126,]),'acao':([82,110,119,126,],[91,91,91,91,]),'se':([82,110,119,126,],[94,94,94,94,]),'repita':([82,110,119,126,],[95,95,95,95,]),'leia':([82,110,119,126,],[96,96,96,96,]),'escreva':([82,110,119,126,],[97,97,97,97,]),'retorna':([82,110,119,126,],[98,98,98,98,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> lista_declaracoes','programa',1,'p_programa','Parser.py',38),
  ('lista_declaracoes -> lista_declaracoes declaracao','lista_declaracoes',2,'p_lista_declaracoes','Parser.py',43),
  ('lista_declaracoes -> declaracao','lista_declaracoes',1,'p_lista_declaracoes1','Parser.py',47),
  ('declaracao -> declaracao_variaveis','declaracao',1,'p_declaracao','Parser.py',53),
  ('declaracao -> inicializacao_variaveis','declaracao',1,'p_declaracao','Parser.py',54),
  ('declaracao -> declaracao_funcao','declaracao',1,'p_declaracao','Parser.py',55),
  ('declaracao_variaveis -> tipo DOIS_PONTOS lista_variaveis','declaracao_variaveis',3,'p_declaracao_variaveis','Parser.py',61),
  ('inicializacao_variaveis -> atribuicao','inicializacao_variaveis',1,'p_inicializacao_variaveis','Parser.py',66),
  ('lista_variaveis -> lista_variaveis VIRGULA var','lista_variaveis',3,'p_lista_variaveis','Parser.py',71),
  ('lista_variaveis -> var','lista_variaveis',1,'p_lista_variaveis1','Parser.py',75),
  ('var -> ID','var',1,'p_var','Parser.py',80),
  ('var -> ID indice','var',2,'p_var1','Parser.py',84),
  ('indice -> indice ABRE_COL expressao FECHA_COL','indice',4,'p_indice','Parser.py',89),
  ('indice -> ABRE_COL expressao FECHA_COL','indice',3,'p_indice1','Parser.py',93),
  ('tipo -> INTEIRO','tipo',1,'p_tipo','Parser.py',97),
  ('tipo -> FLUTUANTE','tipo',1,'p_tipo1','Parser.py',101),
  ('tipo -> CIENTIFICO','tipo',1,'p_tipo2','Parser.py',105),
  ('declaracao_funcao -> tipo cabecalho','declaracao_funcao',2,'p_declaracao_funcao','Parser.py',111),
  ('declaracao_funcao -> cabecalho','declaracao_funcao',1,'p_declaracao_funcao1','Parser.py',115),
  ('cabecalho -> ID ABRE_PAR lista_parametros FECHA_PAR corpo FIM','cabecalho',6,'p_cabecalho','Parser.py',120),
  ('lista_parametros -> lista_parametros VIRGULA parametro','lista_parametros',3,'p_lista_parametros','Parser.py',124),
  ('lista_parametros -> parametro','lista_parametros',1,'p_lista_parametros1','Parser.py',129),
  ('lista_parametros -> vazio','lista_parametros',1,'p_lista_parametros1','Parser.py',130),
  ('parametro -> tipo DOIS_PONTOS ID','parametro',3,'p_parametro','Parser.py',135),
  ('parametro -> parametro ABRE_COL FECHA_COL','parametro',3,'p_parametro1','Parser.py',139),
  ('corpo -> corpo acao','corpo',2,'p_corpo','Parser.py',144),
  ('corpo -> vazio','corpo',1,'p_corpo1','Parser.py',148),
  ('acao -> expressao','acao',1,'p_acao','Parser.py',153),
  ('acao -> declaracao_variaveis','acao',1,'p_acao','Parser.py',154),
  ('acao -> se','acao',1,'p_acao','Parser.py',155),
  ('acao -> repita','acao',1,'p_acao','Parser.py',156),
  ('acao -> leia','acao',1,'p_acao','Parser.py',157),
  ('acao -> escreva','acao',1,'p_acao','Parser.py',158),
  ('acao -> retorna','acao',1,'p_acao','Parser.py',159),
  ('acao -> error','acao',1,'p_acao','Parser.py',160),
  ('se -> SE expressao ENTAO corpo FIM','se',5,'p_se','Parser.py',165),
  ('se -> SE expressao ENTAO corpo SENAO corpo FIM','se',7,'p_se1','Parser.py',171),
  ('repita -> REPITA corpo ATE expressao','repita',4,'p_repita','Parser.py',175),
  ('atribuicao -> var ATRIBUICAO expressao','atribuicao',3,'p_atribuicao','Parser.py',179),
  ('leia -> LEIA ABRE_PAR ID FECHA_PAR','leia',4,'p_leia','Parser.py',183),
  ('escreva -> ESCREVA ABRE_PAR expressao FECHA_PAR','escreva',4,'p_escreva','Parser.py',187),
  ('retorna -> RETORNA ABRE_PAR expressao FECHA_PAR','retorna',4,'p_retorna','Parser.py',191),
  ('expressao -> expressao_simples','expressao',1,'p_expressao','Parser.py',196),
  ('expressao -> atribuicao','expressao',1,'p_expressao','Parser.py',197),
  ('expressao_simples -> expressao_aditiva','expressao_simples',1,'p_expressao_simples','Parser.py',202),
  ('expressao_simples -> expressao_simples operador_relacional expressao_aditiva','expressao_simples',3,'p_expressao_simples1','Parser.py',206),
  ('expressao_aditiva -> expressao_multiplicativa','expressao_aditiva',1,'p_expressao_aditiva','Parser.py',210),
  ('expressao_aditiva -> expressao_aditiva operador_soma expressao_multiplicativa','expressao_aditiva',3,'p_expressao_aditiva1','Parser.py',214),
  ('expressao_multiplicativa -> expressao_unaria','expressao_multiplicativa',1,'p_expressao_multiplicativa','Parser.py',218),
  ('expressao_multiplicativa -> expressao_multiplicativa operador_multiplicacao expressao_unaria','expressao_multiplicativa',3,'p_expressao_multiplicativa1','Parser.py',222),
  ('expressao_unaria -> fator','expressao_unaria',1,'p_expressao_unaria','Parser.py',226),
  ('expressao_unaria -> operador_soma fator','expressao_unaria',2,'p_expressao_unaria1','Parser.py',230),
  ('operador_relacional -> MENOR','operador_relacional',1,'p_operador_relacionar','Parser.py',235),
  ('operador_relacional -> MAIOR','operador_relacional',1,'p_operador_relacionar','Parser.py',236),
  ('operador_relacional -> IGUAL','operador_relacional',1,'p_operador_relacionar','Parser.py',237),
  ('operador_relacional -> DIFERENTE','operador_relacional',1,'p_operador_relacionar','Parser.py',238),
  ('operador_relacional -> MENORIGUAL','operador_relacional',1,'p_operador_relacionar','Parser.py',239),
  ('operador_relacional -> MAIORIGUAL','operador_relacional',1,'p_operador_relacionar','Parser.py',240),
  ('operador_relacional -> E_LOGI','operador_relacional',1,'p_operador_relacionar','Parser.py',241),
  ('operador_relacional -> NEGACAO','operador_relacional',1,'p_operador_relacionar','Parser.py',242),
  ('operador_soma -> ADICAO','operador_soma',1,'p_operador_soma','Parser.py',248),
  ('operador_soma -> SUBTRACAO','operador_soma',1,'p_operador_soma','Parser.py',249),
  ('operador_multiplicacao -> MULTIPLICACAO','operador_multiplicacao',1,'p_operador_multiplicacao','Parser.py',255),
  ('operador_multiplicacao -> DIVISAO','operador_multiplicacao',1,'p_operador_multiplicacao','Parser.py',256),
  ('inteiro -> INTEIRO','inteiro',1,'p_inteiro','Parser.py',261),
  ('flutuante -> FLUTUANTE','flutuante',1,'p_flutuante','Parser.py',266),
  ('fator -> var','fator',1,'p_fator','Parser.py',272),
  ('fator -> chamada_funcao','fator',1,'p_fator','Parser.py',273),
  ('fator -> inteiro','fator',1,'p_fator','Parser.py',274),
  ('fator -> flutuante','fator',1,'p_fator','Parser.py',275),
  ('fator -> ABRE_PAR expressao FECHA_PAR','fator',3,'p_fator1','Parser.py',280),
  ('chamada_funcao -> ID ABRE_PAR lista_argumentos FECHA_PAR','chamada_funcao',4,'p_chamada_funcao','Parser.py',285),
  ('lista_argumentos -> lista_argumentos VIRGULA expressao','lista_argumentos',3,'p_lista_argumentos','Parser.py',289),
  ('lista_argumentos -> expressao','lista_argumentos',1,'p_lista_argumentos1','Parser.py',294),
  ('lista_argumentos -> vazio','lista_argumentos',1,'p_lista_argumentos1','Parser.py',295),
  ('vazio -> <empty>','vazio',0,'p_vazio','Parser.py',300),
]