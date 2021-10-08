# /usr/local/lib/softhsm/lib/softhsm2.so
import pkcs11


# Initialise our PKCS#11 library
# lib = pkcs11.lib(os.environ['PKCS11_MODULE']) #这个是原先的程序的代码，是从环境变量中获取的lib库（共享库so，win下是dll文件）
lib = pkcs11.lib('/usr/local/lib/softhsm/libsofthsm2.so')
print(lib)  # 输出库的信息
# exit()相当于加了个断点
token = lib.get_token(token_label='Token-1')  # 当时自己初始化生成的token label 叫test

data = b'INPUT DATA'

# Open a session on our token
with token.open(user_pin='chi566') as session:  # 这个pin码叫跟出初始化的要相同才行。
    # Generate a DES key in this session
    key = session.generate_key(pkcs11.KeyType.DES3)

    print('key的值为：', ' ', key)

    # Get an initialisation vector
    iv = session.generate_random(64)  # DES blocks are fixed at 64 bits
    print('iv的值为：', ' ', iv)
    # Encrypt our data
    crypttext = key.encrypt(data, mechanism_param=iv)
    print('crypttext的值为：', ' ', crypttext)
