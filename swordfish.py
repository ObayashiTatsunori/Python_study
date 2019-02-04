while True:
  print('あなたはだれ？')
  name=input()
  if name != 'Joe':
    continue
  print('こんにちはJoe。パスワードは何？')
  password = input()
  if password == 'swordfish':
    break
print('認証しました')
