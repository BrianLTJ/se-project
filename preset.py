print(" * Setting up environment")
import os
# Setup os environ
os.environ.setdefault("DJANGO_SETTINGS_MODULE","lms.settings")

# Setup django
import django
django.setup()

from django.contrib.auth.models import User, Permission, ContentType

def create_permissions():
    # Clear Original Permissions
    print(" * Clearing Original Permissions")
    Permission.objects.all().delete()

    print(" * Adding new permissions")

    perms = [['book','bookborrow','用户-查询借阅记录','user_read_borrowlog'],
            ['auth','user','用户-修改用户密码','user_change_password'],
            ['auth','user','管理-入口','admin_entry'],
            ['book','bookborrow','管理-借还书-操作借书','admin_optborrow_borrow'],
            ['book','bookborrow','管理-借还书-操作还书','admin_optborrow_return'],
            ['book','book','管理-书库-图书管理-入口','admin_book_book_entry'],
            ['book','book','管理-书库-图书管理-增加','admin_book_book_add'],
            ['book','book','管理-书库-图书管理-删除','admin_book_book_delete'],
            ['book','book','管理-书库-图书管理-修改','admin_book_book_edit'],
            ['book','libbook','管理-书库-馆藏管理-入口','admin_book_libbook_entry'],
            ['book','libbook','管理-书库-馆藏管理-增加','admin_book_libbook_add'],
            ['book','libbook','管理-书库-馆藏管理-删除','admin_book_libbook_delete'],
            ['book','libbook','管理-书库-馆藏管理-查看','admin_book_libbook_view'],
            ['book','libbook','管理-书库-馆藏管理-修改','admin_book_libbook_edit'],
            ['auth','user','管理-用户-账户管理-入口','admin_user_account_entrance'],
            ['auth','user','管理-用户-账户管理-增加','admin_user_account_add'],
            ['auth','user','管理-用户-账户管理-删除','admin_user_account_delete'],
            ['auth','user','管理-用户-账户管理-查看','admin_user_account_view'],
            ['auth','user','管理-用户-账户管理-修改','admin_user_account_edit'],
            ['auth','group','管理-用户-账户管理-账户改密','admin_user_account_changepsw'],
            ['auth','group','管理-用户-用户组-入口','admin_user_group_entry'],
            ['auth','group','管理-用户-用户组-增加','admin_user_group_add'],
            ['auth','group','管理-用户-用户组-删除','admin_user_group_delete'],
            ['auth','group','管理-用户-用户组-查看','admin_user_group_view'],
            ['auth','group','管理-用户-用户组-修改','admin_user_group_edit'],
            ['auth','permission','管理-用户-权限-查看','admin_user_permissions_view'],
            ['user','borrowright','管理-用户-借书权限组-入口','admin_user_borrowright_entry'],
            ['user','borrowright','管理-用户-借书权限组-增加','admin_user_borrowright_add'],
            ['user','borrowright','管理-用户-借书权限组-删除','admin_user_borrowright_delete'],
            ['user','borrowright','管理-用户-借书权限组-查看','admin_user_borrowright_view'],
            ['user','borrowright','管理-用户-借书权限组-修改','admin_user_borrowright_edit']]

    for item in perms:
        print(" |- "+item[2])
        ct = ContentType.objects.filter(app_label=item[0]).filter(model=item[1]).get()
        Permission.objects.create(content_type=ct, name=item[2], codename=item[3])


def create_superuser_core(username, password):
    user = User.objects.create_user(username=username, password=password)
    user.is_superuser = True
    user.is_staff = True
    user.save()
    print("superuser created")


def create_superuser():
    username = input("Input the username:")
    password = input("Input the password:")
    create_superuser_core(username, password)
    

print("Select the task to execute:")
print("0: All")
print("1: Initialize Permissions")
print("2: Create a superuser")
c = input("Type the code:")
c = int(c)
if c==0:
    create_superuser()
    create_permissions()
elif c==1:
    create_permissions()
elif c==2:
    create_superuser()
else:
    exit()
