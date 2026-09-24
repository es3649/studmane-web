<script setup lang="ts">
import RecipeComponent from '@/components/RecipeComponent.vue';
</script>

<template>
  <RecipeComponent
    name="51: Tomato Mushroom Stew"
    makes="6 servings"
    :game_ingredients="['Tomatoes','Mushrooms']">
    <template #ingredients>
      <ul>
        <li>1lb Mushrooms, quartered</li>
        <li>1 large potato, cubed</li>
        <li>1 onion, chopped</li>
        <li>3 celery stalks, chopped across the grain</li>
        <li>1 can diced tomatoes</li>
        <li>2-4 cloves garlic, minced</li>
        <li>2 Tbs + 1 Tbs oil</li>
        <li>1/2 c red wine</li>
        <li>4c beef broth (or hearty vegetable broth)</li>
        <li>1/3 c + 1/2c water</li>
        <li>1/2 c flour</li>
        <li>1 tsp thyme</li>
        <li>2 bay leaves</li>
        <li>Salt and pepper</li>
      </ul>
    </template>
    <ol>
      <li>Heat 1 Tbs oil in a medium frying pan over medium-high heat, and sauté onions and celery</li>
      <li>In a large soup pot or dutch oven, sauté mushrooms in 1/3c water. Once all liquid has evaporated, add 2 Tbs oil, and sauté mushrooms until they start to brown.</li>
      <li>Add garlic and sauté until fragrant, about 30s</li>
      <li>Deglaze the pot with wine and simmer until it mostly boils off</li>
      <li>Add tomatoes, broth, sautéed vegetables, potatoes, and spices. Bring to a boil, then simmer four 30-45 minutes, until potatoes soften. Season with salt and pepper to taste</li>
      <li>Put 1/2c water in a small mixing bowl. Whisk in flour about 1 Tbs at a time until combined. It should form a thick paste</li>
      <li>While stirring, slowly add the flour paste to the soup. Simmer for a little longer, until the stew thickens</li>
    </ol>
  </RecipeComponent>
</template>