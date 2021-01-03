def automato(teste):
    alfabeto = {"0","1"}
    #estados = {"A","B","C","D"}
    estado_inicial = 'A'
    estados_aceitacao = {'B'}
    tabela_trans ={
        ("A","0") : 'B',
        ('A','1') : 'D',
        ('A','0') : 'B',
        ('B','0') : 'B',
        ('B','1') : 'C',
        ('C','0') : 'B',
        ('C','1') : 'C',
        ('D','0') : 'D',
        ('D','1') : 'D'}
    estado = estado_inicial
    for simbolo in teste:
        if simbolo in alfabeto:
            estado = tabela_trans[(estado,simbolo)]
        else:
            return "Não existe no alfabeto"
    else:
        if estado in estados_aceitacao:
            return  'Sequência aceita'
        else:
            return 'Sequência não aceita'
    

 