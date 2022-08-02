
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ARROW ASSERT BODY BOOL COLON COMMA CONST CURRENT DIV DIVIDE ELSE END ENUM EQU EXPONENT EXTERNFUNCTION EXTERNNODE FALSE FBY FUNCTION GREATER GREATEREQU HASHTAG IF INCLUDE INT INTCONST IS LBPARENTHESE LBRACKET LESS LESSEQU LET LPARENTHESE LSHIFT LV6ID LV6IDREF MERGE MINUS MOD MODEL NEEDS NODE NOEQU NOR NOT OR PACKAGE PLUS POINT PRE PROVIDES RBPARENTHESE RBRACKET REAL REALCONST RETURNS RPARENTHESE RSHIFT SEMICOLON SHIFT STAR STEP STRUCT SURPLUS TEL THEN TPOINT TRUE TYPE UNSAFEEXTERNFUNCTION UNSAFEEXTERNNODE UNSAFEFUNCTION UNSAFENODE USES VAR WHEN WITH XORprogram : packbodypackbody : onedeclonedecl : nodedeclnodedecl : localnodelocalnode : NODE LV6ID staticparams params RETURNS params onetypedecl4 localdecls body localnode1body : LET body1 TELbody1 : equationlist\n             | emptyequationlist : equationequationlist : equation equationlistequation : left EQU expression SEMICOLONleft : leftitemlist\n            | LPARENTHESE leftitemlist RPARENTHESEleftitemlist : leftitemleftitem : LV6IDlocaldecls : localdecllist\n                  | emptylocaldecllist : onelocaldecl localdecllistlocaldecllist : onelocaldeclonelocaldecl : localvarsonelocaldecl : localconstslocalconsts : CONST constdecllistconstdecllist : oneconstdecl SEMICOLON constdecllistconstdecllist : oneconstdecloneconstdecl : LV6ID COLON typelocalvars : VAR vardecllistparams : LPARENTHESE params1 RPARENTHESEparams1 : vardecllist onetypedecl4\n             | emptyvardecllist : vardecl vardecllist1vardecllist1 : SEMICOLON vardecl vardecllist1vardecllist1 : emptyvardecl : typedlv6idstypedlv6ids : LV6ID user1 COLON typeuser1 : COMMA LV6ID user1\n             | emptylocalnode1 : POINT \n                  | onetypedecl4onetypedecl4 : SEMICOLON\n                     | emptyempty :staticparams : LSHIFT staticparamlist RSHIFT\n                    | emptystaticparamlist : staticparam staticparamlist1staticparamlist1 : SEMICOLON staticparam staticparamlist1\n                        | emptystaticparam : type LV6IDtype : type1 type2type1 : BOOL\n             | INT\n             | REAL\n             | LV6IDREFtype2 : EXPONENT expression type2\n             | emptyexpression : constantconstant : TRUE\n                | FALSE\n                | REALCONST\n                | INTCONSTexpression : LV6IDexpression : MINUS expressionexpression : NOT expressionexpression : IF expression THEN expression ELSE expression'
    
_lr_action_items = {'NODE':([0,],[6,]),'$end':([1,2,3,4,5,39,40,79,87,88,89,102,],[0,-1,-2,-3,-4,-39,-40,-41,-38,-5,-37,-6,]),'LV6ID':([6,12,15,16,17,18,19,20,33,34,35,42,45,48,49,50,51,52,53,54,55,56,57,63,64,65,73,74,78,80,93,96,99,101,104,108,111,],[7,27,32,-41,-49,-50,-51,-52,-48,50,-54,27,61,-41,-55,-60,50,50,50,-56,-57,-58,-59,-53,-61,-62,27,85,50,98,98,98,85,50,50,-63,-11,]),'LSHIFT':([7,],[9,]),'LPARENTHESE':([7,8,10,21,28,80,93,111,],[-41,12,-43,12,-42,96,96,-11,]),'BOOL':([9,30,60,100,],[17,17,17,17,]),'INT':([9,30,60,100,],[18,18,18,18,]),'REAL':([9,30,60,100,],[19,19,19,19,]),'LV6IDREF':([9,30,60,100,],[20,20,20,20,]),'RETURNS':([11,37,],[21,-27,]),'RPARENTHESE':([12,16,17,18,19,20,22,23,24,25,26,33,35,38,39,40,41,43,48,49,50,54,55,56,57,59,63,64,65,75,76,97,98,105,108,],[-41,-41,-49,-50,-51,-52,37,-41,-29,-41,-33,-48,-54,-28,-39,-40,-30,-32,-41,-55,-60,-56,-57,-58,-59,-41,-53,-61,-62,-31,-34,-14,-15,110,-63,]),'RSHIFT':([13,14,29,31,32,47,62,],[28,-41,-44,-46,-47,-41,-45,]),'SEMICOLON':([14,16,17,18,19,20,23,25,26,32,33,35,36,37,41,43,47,48,49,50,54,55,56,57,59,63,64,65,75,76,79,84,102,107,108,109,],[30,-41,-49,-50,-51,-52,39,42,-33,-47,-48,-54,39,-27,-30,-32,30,-41,-55,-60,-56,-57,-58,-59,42,-53,-61,-62,-31,-34,39,99,-6,-25,-63,111,]),'EXPONENT':([16,17,18,19,20,48,49,50,54,55,56,57,64,65,108,],[34,-49,-50,-51,-52,34,-55,-60,-56,-57,-58,-59,-61,-62,-63,]),'VAR':([16,17,18,19,20,25,26,33,35,36,37,39,40,41,43,48,49,50,54,55,56,57,58,59,63,64,65,70,71,72,75,76,82,83,84,106,107,108,],[-41,-49,-50,-51,-52,-41,-33,-48,-54,-41,-27,-39,-40,-30,-32,-41,-55,-60,-56,-57,-58,-59,73,-41,-53,-61,-62,73,-20,-21,-31,-34,-26,-22,-24,-23,-25,-63,]),'CONST':([16,17,18,19,20,25,26,33,35,36,37,39,40,41,43,48,49,50,54,55,56,57,58,59,63,64,65,70,71,72,75,76,82,83,84,106,107,108,],[-41,-49,-50,-51,-52,-41,-33,-48,-54,-41,-27,-39,-40,-30,-32,-41,-55,-60,-56,-57,-58,-59,74,-41,-53,-61,-62,74,-20,-21,-31,-34,-26,-22,-24,-23,-25,-63,]),'LET':([16,17,18,19,20,25,26,33,35,36,37,39,40,41,43,48,49,50,54,55,56,57,58,59,63,64,65,67,68,69,70,71,72,75,76,81,82,83,84,106,107,108,],[-41,-49,-50,-51,-52,-41,-33,-48,-54,-41,-27,-39,-40,-30,-32,-41,-55,-60,-56,-57,-58,-59,-41,-41,-53,-61,-62,80,-16,-17,-19,-20,-21,-31,-34,-18,-26,-22,-24,-23,-25,-63,]),'COMMA':([27,61,],[45,45,]),'COLON':([27,44,46,61,77,85,],[-41,60,-36,-41,-35,100,]),'MINUS':([34,51,52,53,78,101,104,],[51,51,51,51,51,51,51,]),'NOT':([34,51,52,53,78,101,104,],[52,52,52,52,52,52,52,]),'IF':([34,51,52,53,78,101,104,],[53,53,53,53,53,53,53,]),'TRUE':([34,51,52,53,78,101,104,],[54,54,54,54,54,54,54,]),'FALSE':([34,51,52,53,78,101,104,],[55,55,55,55,55,55,55,]),'REALCONST':([34,51,52,53,78,101,104,],[56,56,56,56,56,56,56,]),'INTCONST':([34,51,52,53,78,101,104,],[57,57,57,57,57,57,57,]),'THEN':([49,50,54,55,56,57,64,65,66,108,],[-55,-60,-56,-57,-58,-59,-61,-62,78,-63,]),'ELSE':([49,50,54,55,56,57,64,65,86,108,],[-55,-60,-56,-57,-58,-59,-61,-62,101,-63,]),'POINT':([79,102,],[89,-6,]),'TEL':([80,90,91,92,93,103,111,],[-41,102,-7,-8,-9,-10,-11,]),'EQU':([94,95,97,98,110,],[104,-12,-14,-15,-13,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'packbody':([0,],[2,]),'onedecl':([0,],[3,]),'nodedecl':([0,],[4,]),'localnode':([0,],[5,]),'staticparams':([7,],[8,]),'empty':([7,12,14,16,23,25,27,36,47,48,58,59,61,79,80,],[10,24,31,35,40,43,46,40,31,35,69,43,46,40,92,]),'params':([8,21,],[11,36,]),'staticparamlist':([9,],[13,]),'staticparam':([9,30,],[14,47,]),'type':([9,30,60,100,],[15,15,76,107,]),'type1':([9,30,60,100,],[16,16,16,16,]),'params1':([12,],[22,]),'vardecllist':([12,73,],[23,82,]),'vardecl':([12,42,73,],[25,59,25,]),'typedlv6ids':([12,42,73,],[26,26,26,]),'staticparamlist1':([14,47,],[29,62,]),'type2':([16,48,],[33,63,]),'onetypedecl4':([23,36,79,],[38,58,87,]),'vardecllist1':([25,59,],[41,75,]),'user1':([27,61,],[44,77,]),'expression':([34,51,52,53,78,101,104,],[48,64,65,66,86,108,109,]),'constant':([34,51,52,53,78,101,104,],[49,49,49,49,49,49,49,]),'localdecls':([58,],[67,]),'localdecllist':([58,70,],[68,81,]),'onelocaldecl':([58,70,],[70,70,]),'localvars':([58,70,],[71,71,]),'localconsts':([58,70,],[72,72,]),'body':([67,],[79,]),'constdecllist':([74,99,],[83,106,]),'oneconstdecl':([74,99,],[84,84,]),'localnode1':([79,],[88,]),'body1':([80,],[90,]),'equationlist':([80,93,],[91,103,]),'equation':([80,93,],[93,93,]),'left':([80,93,],[94,94,]),'leftitemlist':([80,93,96,],[95,95,105,]),'leftitem':([80,93,96,],[97,97,97,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> packbody','program',1,'p_program_packboy','lustre_complie.py',18),
  ('packbody -> onedecl','packbody',1,'p_packbody1','lustre_complie.py',22),
  ('onedecl -> nodedecl','onedecl',1,'p_onedecl_nodedecl','lustre_complie.py',26),
  ('nodedecl -> localnode','nodedecl',1,'p_nodedecl_localnode','lustre_complie.py',30),
  ('localnode -> NODE LV6ID staticparams params RETURNS params onetypedecl4 localdecls body localnode1','localnode',10,'p_localnode_node1','lustre_complie.py',34),
  ('body -> LET body1 TEL','body',3,'p_body','lustre_complie.py',43),
  ('body1 -> equationlist','body1',1,'p_body1','lustre_complie.py',47),
  ('body1 -> empty','body1',1,'p_body1','lustre_complie.py',48),
  ('equationlist -> equation','equationlist',1,'p_equationlist1_eq','lustre_complie.py',52),
  ('equationlist -> equation equationlist','equationlist',2,'p_equationlist1_eqlist','lustre_complie.py',57),
  ('equation -> left EQU expression SEMICOLON','equation',4,'p_equation_left','lustre_complie.py',63),
  ('left -> leftitemlist','left',1,'p_left','lustre_complie.py',69),
  ('left -> LPARENTHESE leftitemlist RPARENTHESE','left',3,'p_left','lustre_complie.py',70),
  ('leftitemlist -> leftitem','leftitemlist',1,'p_leftitemlist','lustre_complie.py',78),
  ('leftitem -> LV6ID','leftitem',1,'p_leftitem_lv6id','lustre_complie.py',82),
  ('localdecls -> localdecllist','localdecls',1,'p_localdecls','lustre_complie.py',86),
  ('localdecls -> empty','localdecls',1,'p_localdecls','lustre_complie.py',87),
  ('localdecllist -> onelocaldecl localdecllist','localdecllist',2,'p_localdecllist1','lustre_complie.py',91),
  ('localdecllist -> onelocaldecl','localdecllist',1,'p_localdecllist2','lustre_complie.py',95),
  ('onelocaldecl -> localvars','onelocaldecl',1,'p_onelocaldecl_var','lustre_complie.py',99),
  ('onelocaldecl -> localconsts','onelocaldecl',1,'p_onelocaldecl_const','lustre_complie.py',103),
  ('localconsts -> CONST constdecllist','localconsts',2,'p_localconsts','lustre_complie.py',107),
  ('constdecllist -> oneconstdecl SEMICOLON constdecllist','constdecllist',3,'p_constdecllist1','lustre_complie.py',113),
  ('constdecllist -> oneconstdecl','constdecllist',1,'p_constdecllist2','lustre_complie.py',118),
  ('oneconstdecl -> LV6ID COLON type','oneconstdecl',3,'p_oneconstdecl1','lustre_complie.py',122),
  ('localvars -> VAR vardecllist','localvars',2,'p_localvars','lustre_complie.py',129),
  ('params -> LPARENTHESE params1 RPARENTHESE','params',3,'p_params','lustre_complie.py',135),
  ('params1 -> vardecllist onetypedecl4','params1',2,'p_params1','lustre_complie.py',139),
  ('params1 -> empty','params1',1,'p_params1','lustre_complie.py',140),
  ('vardecllist -> vardecl vardecllist1','vardecllist',2,'p_vardecllist','lustre_complie.py',146),
  ('vardecllist1 -> SEMICOLON vardecl vardecllist1','vardecllist1',3,'p_vardecllist1','lustre_complie.py',151),
  ('vardecllist1 -> empty','vardecllist1',1,'p_vardecllist1_empty','lustre_complie.py',156),
  ('vardecl -> typedlv6ids','vardecl',1,'p_vardecl','lustre_complie.py',160),
  ('typedlv6ids -> LV6ID user1 COLON type','typedlv6ids',4,'p_typedlv6ids','lustre_complie.py',164),
  ('user1 -> COMMA LV6ID user1','user1',3,'p_user1','lustre_complie.py',171),
  ('user1 -> empty','user1',1,'p_user1','lustre_complie.py',172),
  ('localnode1 -> POINT','localnode1',1,'p_localnode1','lustre_complie.py',181),
  ('localnode1 -> onetypedecl4','localnode1',1,'p_localnode1','lustre_complie.py',182),
  ('onetypedecl4 -> SEMICOLON','onetypedecl4',1,'p_ondetypedecl4','lustre_complie.py',186),
  ('onetypedecl4 -> empty','onetypedecl4',1,'p_ondetypedecl4','lustre_complie.py',187),
  ('empty -> <empty>','empty',0,'p_empty','lustre_complie.py',191),
  ('staticparams -> LSHIFT staticparamlist RSHIFT','staticparams',3,'p_staticparams','lustre_complie.py',195),
  ('staticparams -> empty','staticparams',1,'p_staticparams','lustre_complie.py',196),
  ('staticparamlist -> staticparam staticparamlist1','staticparamlist',2,'p_staticparamslist','lustre_complie.py',201),
  ('staticparamlist1 -> SEMICOLON staticparam staticparamlist1','staticparamlist1',3,'p_staticparamlist1','lustre_complie.py',205),
  ('staticparamlist1 -> empty','staticparamlist1',1,'p_staticparamlist1','lustre_complie.py',206),
  ('staticparam -> type LV6ID','staticparam',2,'p_staticparam_typelv6id','lustre_complie.py',210),
  ('type -> type1 type2','type',2,'p_type','lustre_complie.py',216),
  ('type1 -> BOOL','type1',1,'p_type1','lustre_complie.py',220),
  ('type1 -> INT','type1',1,'p_type1','lustre_complie.py',221),
  ('type1 -> REAL','type1',1,'p_type1','lustre_complie.py',222),
  ('type1 -> LV6IDREF','type1',1,'p_type1','lustre_complie.py',223),
  ('type2 -> EXPONENT expression type2','type2',3,'p_type2','lustre_complie.py',235),
  ('type2 -> empty','type2',1,'p_type2','lustre_complie.py',236),
  ('expression -> constant','expression',1,'p_expression_constant','lustre_complie.py',241),
  ('constant -> TRUE','constant',1,'p_constant','lustre_complie.py',245),
  ('constant -> FALSE','constant',1,'p_constant','lustre_complie.py',246),
  ('constant -> REALCONST','constant',1,'p_constant','lustre_complie.py',247),
  ('constant -> INTCONST','constant',1,'p_constant','lustre_complie.py',248),
  ('expression -> LV6ID','expression',1,'p_expression_lv6id','lustre_complie.py',262),
  ('expression -> MINUS expression','expression',2,'p_expression_neg','lustre_complie.py',269),
  ('expression -> NOT expression','expression',2,'p_exression_not','lustre_complie.py',278),
  ('expression -> IF expression THEN expression ELSE expression','expression',6,'p_expression_if','lustre_complie.py',287),
]
