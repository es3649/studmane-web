<script setup lang="ts">
import RecipeComponent from '@/components/RecipeComponent.vue'
</script>

<template>
  <RecipeComponent
    name="54: Veggie Cream Soup"
    makes="6-8 servings"
    :game_ingredients="['Rock Salt', '3x Milk', 'Endura Carrot']"
    :ingredients="[
      '2lb (1kg) Carrots, peeled and cut into roughly uniform pieces',
      '12oz (350g) Salt Pork',
      '1 Onion, quartered',
      '1 Leek, roots and greens removed, halved, and cut into 1.5-2 inch segments',
      '3-5 Cloves of garlic',
      '3/4 lb Baby Carrots, chopped into 1/2in pieces',
      '6-8oz (5-6) white or crimini mushrooms, sliced',
      '2T Butter',
      '4c Chicken Broth',
      '1/2t White Pepper',
      '1/4t Nutmeg',
      'Salt to taste',
      'Cream',
      'Parsley',
    ]"
  >
    <ol>
      <li>
        Place carrots (except baby carrots), onion, leek, and garlic in a pot and cover with water.
        Boil until soft, about 20 min
      </li>
      <li>
        Cut salt pork into 1/2in pieces and place in a roasting pan or baking dish. Cook at 500
        degrees, until fat has rendered, about 15 minutes
      </li>
      <li>
        Drain water from vegetables, and puree in a blender with chicken broth as needed to ensure
        smooth blending
      </li>

      <li>Add remaining chicken broth and rendered pork fat to the puree, and return to the pot</li>

      <li>
        Sauté mushrooms, and add them with the chopped baby carrots to the pot. Add spices and salt
        to taste. Bring the soup to a boil, then simmer for about an hour, or until carrots begin to
        soften.
      </li>

      <li>Garnish with cream and parsley</li>
    </ol>
    <template #notes>
      <p>Suggestions: Use more cream in place of the broth, soften baby carrots before adding</p>
    </template>
  </RecipeComponent>
</template>
