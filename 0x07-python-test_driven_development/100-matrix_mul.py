#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    m1 = "m_a must be a list"
    m2 = "m_b must be a list"
    m3 = "m_a must be a list of lists"
    m4 = "m_a must be a list of lists"
    m5 = "m_a can't be empty"
    m6 = "m_b can't be empty"
    m7 = "m_a should contain only integers or floats"
    m8 = "m_b should contain only integers or floats"
    m9 = "each row of m_a must be of the same size"
    m10 = "each row of m_a must be of the same size"
    m11 = "m_a and m_b can't be multiplied"
    if type(m_a) is not list:
        raise TypeError(m1)

    if type(m_b) is not list:
        raise TypeError(m2)

    for l1 in m_a:
        if type(l1) is not list:
            raise TypeError(m3)

    for l2 in m_b:
        if type(l2) is not list:
            raise TypeError(m4)

    if not m_a:
        raise ValueError(m5)

    if not m_b:
        raise ValueError(m6)

    for l3 in range(len(m_a)):
        for l4 in range(len(m_a[l3])):
            if type(m_a[l3][l4]) is not int and type(m_a[l3][l4]) is not float:
                raise TypeError(m7)

    for l5 in range(len(m_a)):
        for l6 in range(len(m_a[l5])):
            if type(m_a[l5][l6]) is not int and type(m_a[l5][l6]) is not float:
                raise TypeError(m8)

    for l7 in m_a:
        if len(l7) != len(m_a[0]):
            raise TypeError(m9)

    for l8 in m_b:
        if len(l8) != len(m_b[0]):
            raise TypeError(m10)

    if len(m_a[0]) == len(m_b):
        lis = []
        for tr in range(len(m_b[0])):
            lis.append(list(map(lambda i: i[tr], m_b)))
        newl = []
        for r in m_a:
            tmp = []
            for c in lis:
                tmp.append(sum(list(map(lambda j: r[j] * c[j],
                                        range(len(m_a[0]))))))
            newl.append(tmp)
        return newl
    else:
        raise TypeError(m11)