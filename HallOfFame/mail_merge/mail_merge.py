"""
Author: Diogo Rodrigues
ID: up201806429
Email: diogo.rodrigues@fe.up.pt
"""
def mail_merge(names, mail_template):
    ret = []
    with open(names) as innames:
        with open(mail_template, 'r') as intemplate:
            template_cont = intemplate.readlines()
            names_cont = innames.readlines()
            names_cont = [s.strip() for s in names_cont]
            for n in names_cont:
                s = ""
                for l in template_cont:
                    s += l.replace("<name>", n)
                ret += [s]
    return ret
print(mail_merge("names.txt", "template.txt"))
