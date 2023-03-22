import re
from kopeechka import MailActivations
from kopeechka.errors import (
    BAD_TOKEN, WAIT_LINK,
    NO_ACTIVATION, ACTIVATION_CANCELED, 
    ACTIVATION_NOT_FOUND, BAD_EMAIL,
    SYSTEM_ERROR
    )


def check(email: str):
    """Функция для валидации email"""

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.match(regex, email):
        return True
    return email


def parse_facebook(text: str) -> str:
    """Парсинг письма с Facebook"""

    result = re.findall(r'код: \d+|code: \d+', text)
    print(result)
    return result[0]


def mailbox_reorder(token, site, email) -> dict:
    """Повторный запрос активации с этой почтой на kopeechka"""

    body = MailActivations(token=token)
    try:
        res = body.mailbox_reorder(site=site, email=email)
        return res.data
    except (BAD_TOKEN, WAIT_LINK,
            NO_ACTIVATION, ACTIVATION_CANCELED, 
            ACTIVATION_NOT_FOUND, BAD_EMAIL,
            SYSTEM_ERROR 
            ) as e:
        return {'status': 'ERROR', 'value': e}


def mailbox_message(token, full, id) -> str:

    body = MailActivations(token=token)
    try:
        res = body.mailbox_get_message(full=full, id=id)
        return res.data
    except (BAD_TOKEN, WAIT_LINK,
            NO_ACTIVATION, ACTIVATION_CANCELED, 
            ACTIVATION_NOT_FOUND, BAD_EMAIL,
            SYSTEM_ERROR 
            ) as e:
        return {'status': 'ERROR', 'value': e}
    

# print(mailbox_reorder(KP_API, site='facebook.com', email='oxelomymy1981@miqkole.store'))
# print(mailbox_message(token=KP_API, full='1', id='1441058116'))
# code = parse_facebook('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional //EN"><html><head><title>Facebook</title><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><style nonce="WkjgQu38">@media all and (max-width: 480px){*[class].ib_t{min-width:100% !important}*[class].ib_row{display:block !important}*[class].ib_ext{display:block !important;padding:10px 0 5px 0;vertical-align:top !important;width:100% !important}*[class].ib_img,*[class].ib_mid{vertical-align:top !important}*[class].mb_blk{display:block !important;padding-bottom:10px;width:100% !important}*[class].mb_hide{display:none !important}*[class].mb_inl{display:inline !important}*[class].d_mb_flex{display:block !important}}.d_mb_show{display:none}.d_mb_flex{display:flex}@media only screen and (max-device-width: 480px){.d_mb_hide{display:none !important}.d_mb_show{display:block !important}.d_mb_flex{display:block !important}}.mb_text h1,.mb_text h2,.mb_text h3,.mb_text h4,.mb_text h5,.mb_text h6{line-height:normal}.mb_work_text h1{font-size:18px;line-height:normal;margin-top:4px}.mb_work_text h2,.mb_work_text h3{font-size:16px;line-height:normal;margin-top:4px}.mb_work_text h4,.mb_work_text h5,.mb_work_text h6{font-size:14px;line-height:normal}.mb_work_text a{color:#1270e9}.mb_work_text p{margin-top:4px}</style></head><body style="margin:0;padding:0;" dir="ltr" bgcolor="#ffffff"><table border="0" cellspacing="0" cellpadding="0" align="center" id="email_table" style="border-collapse:collapse;"><tr><td id="email_content" style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;background:#ffffff;"><table border="0" width="100%" cellspacing="0" cellpadding="0" style="border-collapse:collapse;"><tr style=""><td height="20" style="line-height:20px;" colspan="3">&nbsp;</td></tr><tr><td height="1" colspan="3" style="line-height:1px;"><span style="color:#FFFFFF;font-size:1px;opacity:0;">\xa0 Hi Эдит, \xa0 You recently added vnachinatel4137&#064;miqkole.store to your Facebook account. \xa0 Please confirm this email address so that we can update your contact information. \xa0 You may be asked to enter this confirmation code: 95778. \xa0 \xa0 Confirm \xa0 \xa0 Thanks, The Facebook team \xa0</span></td></tr><tr><td width="15" style="display:block;width:15px;">&nbsp;&nbsp;&nbsp;</td><td style=""><table border="0" width="100%" cellspacing="0" cellpadding="0" style="border-collapse:collapse;"><tr style=""><td height="15" style="line-height:15px;" colspan="3">&nbsp;</td></tr><tr><td width="32" align="left" valign="middle" style="height:32;line-height:0px;"><a href="https://www.facebook.com/n/?help%2Fsignup&amp;aref=1666259065228105&amp;medium=email&amp;mid=5eb73e219c877G5b0748891aaaG5eb742bafcb49G142&amp;n_m=vnachinatel4137%40miqkole.store&amp;rms=v2&amp;irms=true" style="color:#1b74e4;text-decoration:none;"><img width="32" src="https://static.xx.fbcdn.net/rsrc.php/v3/yc/r/I92GqZOkKcu.png" height="32" style="border:0;" /></a></td><td width="15" style="display:block;width:15px;">&nbsp;&nbsp;&nbsp;</td><td width="100%" style=""><a href="https://www.facebook.com/n/?help%2Fsignup&amp;aref=1666259065228105&amp;medium=email&amp;mid=5eb73e219c877G5b0748891aaaG5eb742bafcb49G142&amp;n_m=vnachinatel4137%40miqkole.store&amp;rms=v2&amp;irms=true" style="color:#1877f2;text-decoration:none;font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:19px;line-height:32px;">Confirm email</a></td></tr><tr style="border-bottom:solid 1px #e5e5e5;"><td height="15" style="line-height:15px;" colspan="3">&nbsp;</td></tr></table></td><td width="15" style="display:block;width:15px;">&nbsp;&nbsp;&nbsp;</td></tr><tr><td width="15" style="display:block;width:15px;">&nbsp;&nbsp;&nbsp;</td><td style=""><table border="0" width="100%" cellspacing="0" cellpadding="0" style="border-collapse:collapse;"><tr style=""><td height="28" style="line-height:28px;">&nbsp;</td></tr><tr><td style=""><span class="mb_text" style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:16px;line-height:21px;color:#141823;">Hi Эдит,</span></td></tr><tr style=""><td height="28" style="line-height:28px;">&nbsp;</td></tr><tr><td style=""><span class="mb_text" style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:16px;line-height:21px;color:#141823;">You recently added <span class="mb_text" style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:16px;line-height:21px;font-weight:bold;color:#141823;">vnachinatel4137&#064;miqkole.store</span> to your Facebook account.</span></td></tr><tr style=""><td height="28" style="line-height:28px;">&nbsp;</td></tr><tr><td style=""><span class="mb_text" style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:16px;line-height:21px;color:#141823;">Please confirm this email address so that we can update your contact information.</span></td></tr><tr style=""><td height="28" style="line-height:28px;">&nbsp;</td></tr><tr><td style=""><span class="mb_text" style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:16px;line-height:21px;color:#141823;">You may be asked to enter this confirmation code: 95778.</span></td></tr><tr style=""><td height="28" style="line-height:28px;">&nbsp;</td></tr><tr><td style=""><table border="0" width="100%" cellspacing="0" cellpadding="0" style="border-collapse:collapse;"><tr style=""><td height="2" style="line-height:2px;" colspan="3">&nbsp;</td></tr><tr><td class="mb_blk" style=""><a href="https://www.facebook.com/confirmcontact.php?c=95778&amp;z=0&amp;gfid=AQC8gwmrVDQ9RnesIUA" style="color:#1b74e4;text-decoration:none;"><table border="0" width="100%" cellspacing="0" cellpadding="0" style="border-collapse:collapse;"><tr><td style="border-collapse:collapse;border-radius:6px;text-align:center;display:block;background:#1877f2;padding:8px 16px 10px 16px;"><a href="https://www.facebook.com/confirmcontact.php?c=95778&amp;z=0&amp;gfid=AQC8gwmrVDQ9RnesIUA" style="color:#1b74e4;text-decoration:none;display:block;"><center><font size="3"><span style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;white-space:nowrap;font-weight:bold;vertical-align:middle;color:#ffffff;font-size:14px;line-height:14px;">Confirm</span></font></center></a></td></tr></table></a></td><td width="100%" class="mb_hide" style=""></td></tr><tr style=""><td height="32" style="line-height:32px;" colspan="3">&nbsp;</td></tr></table></td></tr><tr style=""><td height="28" style="line-height:28px;">&nbsp;</td></tr><tr><td style=""><span class="mb_text" style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:16px;line-height:21px;color:#141823;">Thanks,<br />The Facebook team</span></td></tr><tr style=""><td height="28" style="line-height:28px;">&nbsp;</td></tr></table></td><td width="15" style="display:block;width:15px;">&nbsp;&nbsp;&nbsp;</td></tr><tr><td width="15" style="display:block;width:15px;">&nbsp;&nbsp;&nbsp;</td><td style=""><table border="0" width="100%" cellspacing="0" cellpadding="0" align="left" style="border-collapse:collapse;"><tr style="border-top:solid 1px #e5e5e5;"><td height="19" style="line-height:19px;">&nbsp;</td></tr><tr><td style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:11px;color:#aaaaaa;line-height:16px;"><table border="0" cellspacing="0" cellpadding="0" style="border-collapse:collapse;"><tr><td align="center" style="font-size:11px;font-family:LucidaGrande,tahoma,verdana,arial,sans-serif;padding-bottom:6px;">from</td></tr><tr><td align="center" style="font-size:11px;font-family:LucidaGrande,tahoma,verdana,arial,sans-serif;padding-top:6px;padding-bottom:6px;"><img width="74" alt="Meta" height="22" src="https://facebook.com/images/email/meta_logo.png" style="border:0;" /></td></tr><tr><td align="center" style="font-size:11px;font-family:LucidaGrande,tahoma,verdana,arial,sans-serif;padding-top:6px;padding-bottom:6px;">© Facebook. Meta Platforms, Inc., Attention: Community Support, 1 Facebook Way, Menlo Park, CA 94025</td></tr><tr><td align="center" style="font-size:11px;font-family:LucidaGrande,tahoma,verdana,arial,sans-serif;padding-top:6px;">This message was sent to <a style="color:#1b74e4;text-decoration:none;" href="mailto:vnachinatel4137&#064;miqkole.store">vnachinatel4137&#064;miqkole.store</a>. <br />To help keep your account secure, please don&#039;t forward this email. <a style="color:#1b74e4;text-decoration:none;" href="https://www.facebook.com/help/213481848684090/">Learn more</a></td></tr></table><tr style=""><td height="10" style="line-height:10px;">&nbsp;</td></tr></td></tr></table></td><td width="15" style="display:block;width:15px;">&nbsp;&nbsp;&nbsp;</td></tr><tr style=""><td height="20" style="line-height:20px;" colspan="3">&nbsp;</td></tr></table><span style=""><img src="https://www.facebook.com/email_open_log_pic.php?cn=tnz0I16VVq&amp;mid=5eb73e219c877G5b0748891aaaG5eb742bafcb49G142" style="border:0;width:1px;height:1px;" /></span></td></tr></table></body></html>\n\n\n\n')

