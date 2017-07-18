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
assert parse('iszero(true)') == 'Error: iszero espera un valor de tipo Nat'
print 'Caso: iszero(true) OK!'
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

print '\nTesteando lambdas sin aplicacion:\n'

assert parse('\\z:Nat.z') == '\\z:Nat.z:Nat->Nat'
print 'Caso: \\z:Nat.z OK!'
assert parse('\\z:Nat.succ(z)') == '\\z:Nat.succ(z):Nat->Nat'
print 'Caso: \\z:Nat.succ(z) OK!'
assert parse('\\z:Nat.pred(z)') == '\\z:Nat.pred(z):Nat->Nat'
print 'Caso: \\z:Nat.pred(z) OK!'
assert parse('\\z:Nat.true') == '\\z:Nat.true:Nat->Bool'
print 'Caso: \\z:Nat.true OK!'
assert parse('\\z:Nat.iszero(z)') == '\\z:Nat.iszero(z):Nat->Bool'
print 'Caso: \\z:Nat.iszero(z) OK!'
assert parse('\\z:Nat.if z then 0 else succ(0)') == '\\z:Nat.if z then 0 else succ(0):Nat->Nat'
print 'Caso: \\z:Nat.\\y:Bool.if y then z else succ(z) OK!'
print parse('\\z:Nat.\\y:Bool.if y then z else succ(z)')
assert parse('\\z:Nat.\\y:Bool.if y then z else succ(z)') == '\\z:Nat.\\y:Bool.if y then z else succ(z):Nat->Bool->Nat'
print 'Caso: \\z:Nat.\\y:Bool.if y then z else succ(z) OK!'


print '\nTesteando lambdas con aplicacion:\n'

print parse('(\\z:Nat.z) 0')
assert parse('(\\z:Nat.z) 0') == '0:Nat'
print 'Caso: (\\z:Nat.z) 0 OK!'
assert parse('(\\z:Nat.succ(z)) 0') == 'succ(0):Nat'
print 'Caso: (\\z:Nat.succ(z)) 0 OK!'
assert parse('(\\z:Nat.succ(succ(z))) 0') == 'succ(succ(0)):Nat'
print 'Caso: (\\z:Nat.succ(succ(z))) 0 OK!'
assert parse('(\\z:Nat.pred(succ(succ(z)))) 0') == 'succ(0):Nat'
print 'Caso: (\\z:Nat.pred(succ(succ(z)))) 0 OK!'
assert parse('(\\z:Nat.z)  true') == 'true:Bool'
print 'Caso: (\\z:Nat.z)  true OK!'
assert parse('(\\z:Nat.z)  false') == 'false:Bool'
print 'Caso: (\\z:Nat.z)  false OK!'
assert parse('(\\z:Nat.iszero(z)) 0') == 'true:Bool'
print 'Caso: (\\z:Nat.iszero(z)) 0 OK!'
assert parse('(\\z:Nat.iszero(succ(z))) 0') == 'false:Bool'
print 'Caso: (\\z:Nat.iszero(succ(z))) 0 OK!'
assert parse('(\\z:Nat.if z then 0 else succ(0)) false') == 'succ(0):Nat'
print 'Caso: (\\z:Nat.if z then 0 else succ(0)) false OK!'
assert parse('(\\z:Nat.if z then 0 else succ(0)) true') == '0:Nat'
print 'Caso: (\\z:Nat.if z then 0 else succ(0)) true OK!'
assert parse('(\\z:Nat.if z then 0 else succ(0)) iszero(0)') == '0:Nat'
print 'Caso: (\\z:Nat.if z then 0 else succ(0)) iszero(0) OK!'
assert parse('(\\z:Nat.if z then 0 else succ(0)) iszero(succ(0))') == 'succ(0):Nat'
print 'Caso: (\\z:Nat.if z then 0 else succ(0)) iszero(succ(0)) OK!'
assert parse('(\\z:Nat.if iszero(z) then succ(0) else succ(z)) succ(pred(succ(0)))') == 'succ(succ(0)):Nat'
print 'Caso: (\\z:Nat.if iszero(z) then succ(0) else succ(z)) succ(pred(succ(0))) OK!'

print '\nTesteando lambdas con y sin aplicacion complejos:\n'

assert parse('(\\x:Bool.(\\z:Nat.if x then z else succ(z))) true 0') == '0:Nat'
print 'Caso: (\\x:Bool.(\\z:Nat.if x then z else succ(z))) true 0 OK!'
assert parse('(\\x:Nat->Nat.(\\y:Nat. (\\z:Bool.if z then x y else 0))) (\\j:Nat.succ(j)) succ(succ(0)) true') == 'succ(succ(succ(0))):Nat'
print 'Caso: (\\x:Nat->Nat.(\\y:Nat. (\\z:Bool.if z then x y else 0))) (\\j:Nat.succ(j)) succ(succ(0)) true OK!'
assert parse('(\\z:Nat.iszero(pred(z))) succ(0)') == 'true:Bool'
print 'Caso: (\\z:Nat.iszero(pred(z))) succ(0) OK!'
assert parse('(\\x:Nat->Nat.x) (\\j:Nat.succ(j))') == '\\j:Nat.succ(j):(Nat->Nat)'
print 'Caso: (\\x:Nat->Nat.x) (\\j:Nat.succ(j)) OK!'
assert parse('(\\x:Nat->Nat.(\\y:Nat. (\\z:Bool.if z then x y else 0))) (\\j:Nat.succ(j)) succ(succ(0)) false') == '0:Nat'
print 'Caso: (\\x:Nat->Nat.(\\y:Nat. (\\z:Bool.if z then x y else 0))) (\\j:Nat.succ(j)) succ(succ(0)) false OK!'

print '\nTesteando ejemplos enunciado:\n'

print parse('0')
print parse('true')
print parse('if true then 0 else false')
print parse('\\x:Bool.if x then false else true')
print parse('\\x:Nat.succ(0)')
print parse('\\z:Nat.z')
print parse('succ(succ(succ(0)))')
print parse('succ(succ(pred(0)))')
print parse('\\x:Nat.succ(x)')
print parse('0 0')
print parse('\\x:Nat->Nat.\\y:Nat.(\\z:Bool.if z then x y else 0)')
print parse('(\\x:Nat->Nat.(\\y:Nat. (\\z:Bool.if z then x y else 0))) (\\j:Nat.succ(j)) succ(succ(succ(succ(succ(succ(succ(succ(0)))))))) true')

print '\nTesting finalizado, todos los casos correctos!\n'
