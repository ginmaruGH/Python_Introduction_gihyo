## Chapter10 ファイルと例外
### ファイルを読み込む
#### ファイル全体を読み込む

print("\nファイル全体を読み込む\n")

# filename = 'pi_digits.txt'
filename = 'chap_10/pi_digits.txt'

with open(filename) as file_object:
    contents = file_object.read()
print(contents)
# 余分な空行を取り除く
print(contents.rstrip())
