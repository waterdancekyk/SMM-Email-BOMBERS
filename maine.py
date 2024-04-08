from social_spam import mail

mail = mail()
mail.connect_mail ('','')

mail.set_message('','')
mail.bombing_message('', amount=10); 

#mail.connect_mail - данные с почты которой будут отправляться
#mail.set_message - тема и описание.
#mail.bombing_message - почта на которую должны поступить сообщение и сколько кругов.

#mail.connect_mail - data from which mail will be sent
#mail.set_message - subject and description.
#mail.bombing_message - the mail to which the message should arrive and how many circles.