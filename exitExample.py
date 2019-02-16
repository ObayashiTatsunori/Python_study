import sys
while True:
  print('終了するためにはexitと入力してください。')
  responce = input()
  if responce == 'exit':
    sys.exit()
  print(responce+'と入力されました')