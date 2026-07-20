<script setup lang="ts">
import RecipeComponent from '@/components/RecipeComponent.vue'
</script>
<template>
  <RecipeComponent
    name="133: Noble Pursuit"
    :game_ingredients="['Palm Fruit', 'Hydromelon', 'Voltfruit', 'Salt']"
    makes="3 servings"
  >
    <template #notes>
      <p>
        This is a mild-flavored, highly refreshing drink. It has a hint of savoriness, and a light
        sweetness. The salt and acid of the lime really makes the flavors pop.
      </p>
    </template>
    <template #ingredients>
      <ul>
        <li>1/2 Dragonfruit</li>
        <li>1 coconut of coconut milk</li>
        <li>8 oz honeydew melon?</li>
        <li>1 lime, quartered</li>
        <li>8oz of 7 Up (about 2/3 of a can)</li>
        <li>2 tsp sugar</li>
        <li>pinch of Salt</li>
      </ul>
    </template>
    <ol>
      <li>
        Chop melon into 1/2 inch pieces, and place in a small saucepan with juice of one lime
        quarter, and sugar. Mix and simmer over medium-high heat until liquid is produced and is
        boiling. Remove from heat and allow to cool.
      </li>
      <li>Purée melon mixture in blender.</li>
      <li>
        Scoop dragonfruit from husk and add to the blender. Blend until the dragonfruit is almost
        puréed
      </li>
      <li>
        Mix in coconut milk, 7 Up, and salt. Serve with a slice of lime. Garnish with a strip of
        dragonfruit husk for a fancy look.
      </li>
    </ol>
  </RecipeComponent>
</template>
