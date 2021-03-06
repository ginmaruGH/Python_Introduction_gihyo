# 7-10.夢のバケーション
print("\n# 7-10.夢のバケーション\n")

name_prompt = "\nあたなのお名前は？ >> "
place_prompt = "世界中どこでも好きなところに行けるとしたら、どこへ行きたいですか？ >> "
continue_prompt = "\n誰かほかの回答してくれる人はいますか？（yes/no）"

# Responses will be stored in the form {name: place}.
responses = {}

while True:
    # Ask the user where they'd like to go.
    name = input(name_prompt)
    place = input(place_prompt)

    # Store the response.
    responses[name] = place

    # Ask if there's anyone else responding.
    repeat = input(continue_prompt)
    if repeat != 'yes':
        break

# Show results of the survey.
print("\n--- 投票結果 ---")
for name, place in responses.items():
    print(f"{name.title()}さんが行きたい場所は、{place.title()}です。")
