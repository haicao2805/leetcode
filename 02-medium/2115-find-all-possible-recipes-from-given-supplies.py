class Solution:
    def findAllRecipes(
        self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]
    ) -> list[str]:
        canCook = {s: True for s in supplies}
        recipeIdx = {r: i for i, r in enumerate(recipes)}

        def dfs(recipe: str) -> bool:
            if recipe in canCook:
                return canCook[recipe]
            if recipe not in recipeIdx:
                return False

            canCook[recipe] = False
            for nei in ingredients[recipeIdx[recipe]]:
                if not dfs(nei):
                    return False
            canCook[recipe] = True
            return canCook[recipe]

        return [r for r in recipes if dfs(r)]


if __name__ == "__main__":
    s = Solution()
    print(
        s.findAllRecipes(
            recipes=["bread"],
            ingredients=[["yeast", "flour"]],
            supplies=["yeast"],
        )
    )
    print(
        s.findAllRecipes(
            recipes=["bread"],
            ingredients=[["yeast", "flour"]],
            supplies=["yeast", "flour", "corn"],
        )
    )
    print(
        s.findAllRecipes(
            recipes=["bread", "sandwich"],
            ingredients=[["yeast", "flour"], ["bread", "meat"]],
            supplies=["yeast", "flour", "meat"],
        )
    )
    print(
        s.findAllRecipes(
            recipes=["bread", "sandwich", "burger"],
            ingredients=[
                ["yeast", "flour"],
                ["bread", "meat"],
                ["sandwich", "meat", "bread"],
            ],
            supplies=["yeast", "flour", "meat"],
        )
    )
