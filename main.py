import cfg
import generate
from lustre_lex import lexer, get_tokens, token2string, getNfadir
from recognition import Recognition

def ouput_result(pda, tokens):
    # 打印词法分析结果
    print("Tokens:")
    print("===========")
    for string_token in tokens:
        # print(token2string(string_token))
        print(string_token)
    print("===========")

    flag = input("是否输出词法分析对应的nfa:(y/n)")
    if flag is "y":
        print("===========")
        nfa_dir = getNfadir()
        for token in tokens:
            nfa = nfa_dir[token.type]
            print("类型: %10s, 开始状态:%5s, 结束状态:%5s, 状态个数:%5s, NFA:%s"
                  %(token.type.strip(), nfa[3].strip(), nfa[4].strip(), nfa[2].strip(), nfa[5:]))
        print("===========")

    flag = input("是否输出文法对应的下推自动机:(y/n)")
    # 打印下推自动机
    if flag is "y":
        print("===========")
        print("Pda:")
        print(pda)
        print("===========")


if __name__ == '__main__':
    grammarString = ""
    with open("data/lustre_no_rec.txt") as r_f:
        for line in r_f.readlines():
            grammarString += line

    inputString = '''
    node EDGE (X: bool) returns (Y: bool);
    let
        Y = not (X);
    tel
    '''
    # 关键字、变量名、符号
    string_tokens = get_tokens(inputString)
    grammar, pda = cfg.create_pda(grammarString)

    may_empty_nonterminal = cfg.get_may_empty_nonterminal(grammar)

    ouput_result(pda, string_tokens)

# # 文法单元 -> 前置条件/后置条件
# # 文法单元 -> 下推自动机  ++
# # 文法单元 -> 目标码 C --> misrC  -- **
# # 文法单元 -> 证明序列 （+证明的证据）
# # 文法单元 -> 证明序列的验证



    print("Recognition:")
    reconigtion = Recognition(pda, string_tokens, may_empty_nonterminal)
    result = reconigtion.is_accept('Start',0)
    print("===========")

    # used = unique_list(reconigtion.used)
    # print(used)
    for i in reversed(reconigtion.used):
        print("~~:", i)

#     # g = generate.Generate()
#     # print(g.gen_node())
#     # print(g.gen_not())

#     print()

#     if result:
#         print("result : True")
#     else:
#         print("result : False")
    # String_2 = '''
    # node r_edge (X: bool) returns (Y: bool);
    # let
    #  Y = false -> X and not pre(X);
    # tel
    # '''
