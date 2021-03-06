# Python Crash Course [First Part]

最短距離でゼロからしっかり学ぶPython入門「必修編」

[サポートページ GitHub](https://github.com/takanory/saitan-python)

[Original Support site](https://nostarch.com/pythoncrashcourse2e)

[Coding is political](https://ehmatthes.github.io/pcc_2e/)

[Original GitHub](https://github.com/ehmatthes/pcc_2e/)

[The Zen of Python 解題 - 前編](https://atsuoishimoto.hatenablog.com/entry/20100920/1284986066)

[The Zen of Python 解題 - 後編](https://atsuoishimoto.hatenablog.com/entry/20100926/1285508015)

---

## Chapter11 コードをテストする

### 関数をテストする

- name_function.py
- names.py

#### ユニットテストとテストケース

- unittestモジュール
  - ユニットテスト（単体テスト）
  - テストケース（ユニットテストの集まり）
- フルカバレッジ
  - 関数が受け取る可能性のある全種類の入力を考慮し、各パターンの処理を検証する
  - 関数の使い方として可能なものをすべて網羅したユニットテスト

- name_function.py
- test_name_function.py

#### テストに失敗する

- name_function2.py
- test_name_function2.py

#### 失敗したテストに対処する

- name_function3.py
- test_name_function3.py

#### 新しいテストを追加する

- name_function3.py
- test_name_function4.py

---

### クラスをテストする

#### さまざまなassertメソッド

- `unittest.TestCase`クラスの`assert`メソッド
  - `assertEqual(a, b)`
    - aとbが等しい（a == b）
  - `assertNotEqual(a, b)`
    - aとbが等しくない（a != b）
  - `assertTrue(x)`
    - xがTrueである
  - `assertFalse(x)`
    - xがFalseである
  - `assertIn(item, list)`
    - itemがlistの中にある
  - `assertNotIn(item, list)`
    - itemがlistの中にない

#### テスト対象のクラス

- survey.py
- language_survey.py

#### AnonymousSurveyクラスをテストする

- test_survey.py
- survey.py

#### setUp()メソッド

- test_survey2.py
- survey.py

