password = 'a123456'
i = 0
while i < 3 :
	psd = input('請輸入密碼: ')
	if psd == password :
		print('恭喜正確')
		break
	else :
		i = i + 1
		print('輸入第', i , '次錯誤 ,還有', 3-i ,'次機會')