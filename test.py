from analyzer import parse

print 'Testeando casos basicos:\n'

assert parse('0') == '0:Nat'
print 'Caso: 0 OK!'
assert parse('true') == 'True:Bool'
print 'Caso: true OK!'
assert parse('false') == 'False:Bool'
print 'Caso: false OK!'
assert parse('iszero(0)') == 'True:Bool'
print 'Caso: iszero(0) OK!'
assert parse('iszero(0)') == 'True:Bool'
print 'Caso: iszero(0) OK!'
assert parse('succ(0)') == '1:Nat'
print 'Caso: succ(0) OK!'
assert parse('pred(0)') == '0:Nat'
print 'Caso: pred(0) OK!'
assert parse('iszero(pred(0))') == 'True:Bool'
print 'Caso: iszero(pred(0)) OK!'
assert parse('iszero(succ(0))') == 'False:Bool'
print 'Caso: iszero(succ(0)) OK!'
assert parse('if true then 0 else succ(0)') == '0:Nat'
print 'Caso: if true then 0 else succ(0) OK!'
assert parse('if true then false else true') == 'False:Bool'
print 'Caso: if true then false else true OK!'

print '\nTesteando casos combinados:\n'

assert parse('succ(succ(0))') == '2:Nat'
print 'Caso: succ(succ(0)) OK!'
assert parse('succ(pred(0))') == '1:Nat'
print 'Caso: succ(pred(0)) OK!'
assert parse('pred(succ(0))') == '0:Nat'
print 'Caso: pred(succ(0)) OK!'
assert parse('pred(pred(0))') == '0:Nat'
print 'Caso: pred(pred(0)) OK!'
assert parse('if if false then true else false then false else true') == 'True:Bool'
print 'Caso: if if false then true else false then false else true OK!'
assert parse('if iszero(0) then succ(0) else 0') == '1:Nat'
print 'Caso: if iszero(0) then succ(0) else 0 OK!'

print '\nTesteando casos complejos:\n'

assert parse('pred(pred(succ(succ(0))))') == '0:Nat'
print 'Caso: pred(pred(succ(succ(0)))) OK!'
assert parse('succ(pred(pred(succ(succ(0)))))') == '1:Nat'
print 'Caso: succ(pred(pred(succ(succ(0))))) OK!'
assert parse('if iszero(succ(0)) then 0 else if true then pred(succ(0)) else succ(0)') == '0:Nat'
print 'Caso: if iszero(succ(0)) then 0 else if true then pred(succ(0)) else succ(0) OK!'
assert parse('succ(if iszero(0) then succ(0) else 0)') == '2:Nat'
print 'Caso: succ(if iszero(0) then succ(0) else 0) OK!'