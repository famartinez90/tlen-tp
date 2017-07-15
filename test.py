from analyzer import parse

print 'Testeando casos basicos:\n'

assert parse('0') == '0:Nat'
print 'Caso: 0 OK!'
assert parse('true') == 'true:Bool'
print 'Caso: true OK!'
assert parse('false') == 'false:Bool'
print 'Caso: false OK!'
assert parse('iszero(0)') == 'true:Bool'
print 'Caso: iszero(0) OK!'
assert parse('succ(0)') == 'succ(0):Nat'
print 'Caso: succ(0) OK!'
assert parse('pred(0)') == '0:Nat'
print 'Caso: pred(0) OK!'
assert parse('iszero(pred(0))') == 'true:Bool'
print 'Caso: iszero(pred(0)) OK!'
assert parse('iszero(succ(0))') == 'false:Bool'
print 'Caso: iszero(succ(0)) OK!'
assert parse('if true then 0 else succ(0)') == '0:Nat'
print 'Caso: if true then 0 else succ(0) OK!'
assert parse('if true then false else true') == 'false:Bool'
print 'Caso: if true then false else true OK!'

print '\nTesteando casos combinados:\n'

assert parse('succ(succ(0))') == 'succ(succ(0)):Nat'
print 'Caso: succ(succ(0)) OK!'
assert parse('succ(pred(0))') == 'succ(0):Nat'
print 'Caso: succ(pred(0)) OK!'
assert parse('pred(succ(0))') == '0:Nat'
print 'Caso: pred(succ(0)) OK!'
assert parse('pred(pred(0))') == '0:Nat'
print 'Caso: pred(pred(0)) OK!'
assert parse('if if false then true else false then false else true') == 'true:Bool'
print 'Caso: if if false then true else false then false else true OK!'
assert parse('if iszero(0) then succ(0) else 0') == 'succ(0):Nat'
print 'Caso: if iszero(0) then succ(0) else 0 OK!'

print '\nTesteando casos complejos:\n'

assert parse('pred(pred(succ(succ(0))))') == '0:Nat'
print 'Caso: pred(pred(succ(succ(0)))) OK!'
assert parse('succ(pred(pred(succ(succ(0)))))') == 'succ(0):Nat'
print 'Caso: succ(pred(pred(succ(succ(0))))) OK!'
assert parse('if iszero(succ(0)) then 0 else if true then pred(succ(0)) else succ(0)') == '0:Nat'
print 'Caso: if iszero(succ(0)) then 0 else if true then pred(succ(0)) else succ(0) OK!'
assert parse('succ(if iszero(0) then succ(0) else 0)') == 'succ(succ(0)):Nat'
print 'Caso: succ(if iszero(0) then succ(0) else 0) OK!'

print '\nTesteando lambdas con aplicacion:\n'

assert parse('\\z:Nat.z 0') == '0:Nat'
print 'Caso: \\z:Nat.z 0 OK!'

assert parse('\\z:Nat.succ(z) 0') == 'succ(0):Nat'
print 'Caso: \\z:Nat.succ(z) 0 OK!'

assert parse('\\z:Nat.succ(succ(z)) 0') == 'succ(succ(0)):Nat'
print 'Caso: \\z:Nat.succ(succ(z)) 0 OK!'

assert parse('\\z:Nat.pred(succ(succ(z))) 0') == 'succ(0):Nat'
print 'Caso: \\z:Nat.pred(succ(succ(z))) 0 OK!'

assert parse('\\z:Nat.z  true') == 'true:Bool'
print 'Caso: \\z:Nat.z  true OK!'

assert parse('\\z:Nat.z  false') == 'false:Bool'
print 'Caso: \\z:Nat.z  false OK!'

assert parse('\\z:Nat.iszero(z) 0') == 'true:Bool'
print 'Caso: \\z:Nat.iszero(z) 0 OK!'

assert parse('\\z:Nat.iszero(succ(z)) 0') == 'false:Bool'
print 'Caso: \\z:Nat.iszero(succ(z)) 0 OK!'

assert parse('\\z:Nat.if z then 0 else succ(0) false') == 'succ(0):Nat'
print 'Caso: \\z:Nat.if z then 0 else succ(0) false OK!'

assert parse('\\z:Nat.if z then 0 else succ(0) true') == '0:Nat'
print 'Caso: \\z:Nat.if z then 0 else succ(0) true OK!'

assert parse('\\z:Nat.if z then 0 else succ(0) iszero(0)') == '0:Nat'
print 'Caso: \\z:Nat.if z then 0 else succ(0) iszero(0) OK!'

assert parse('\\z:Nat.if z then 0 else succ(0) iszero(succ(0))') == 'succ(0):Nat'
print 'Caso: \\z:Nat.if z then 0 else succ(0) iszero(succ(0)) OK!'

assert parse('\\z:Nat.if iszero(z) then succ(0) else succ(z) succ(pred(succ(0)))') == 'succ(succ(0)):Nat'
print 'Caso: \\z:Nat.if iszero(z) then succ(0) else succ(z) succ(pred(succ(0))) OK!'

print '\nTesteando lambdas con aplicacion complejos:\n'


assert parse('\\x:Bool.(\\z:Nat.if x then z else succ(z)) 0 true') == '0:Nat'
print 'Caso: (\\x:Bool.(\\z:Nat.if x then z else succ(z))) 0 true OK!'

print parse('(\\z:Nat.iszero((\\x:Nat. pred(x)) z)) succ(0)')
assert parse('(\\z:Nat.iszero((\\x:Nat. pred(x)) z)) succ(0)') == 'true:Bool'



print '\nTesting finalizado, todos los casos correctos!\n'
