# -- coding: utf-8 --

#���ȣ�����һ������֤���û��б�
# ��һ�����ڴ�������֤�û��Ŀ��б�

unconfirmed_users = ['alice','brian','candace']
confirmed_users = []

#��֤ÿ���û���ֱ��û��δ��֤�û�Ϊֹ
# ��ÿ��������֤���û����ƶ�������֤�б���

while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	print("Verifying user:" + current_user.title())
	confirmed_users.append(current_user)
	
#��ʾ��������֤���û�
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())
