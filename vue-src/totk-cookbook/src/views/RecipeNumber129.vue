<script setup lang="ts">
import RecipeComponent from '@/components/RecipeComponent.vue';
</script>

<template>
  <RecipeComponent
    name="129: Cheesecake"
    makes="16-20 servings (makes two cheesecakes)"
    :game_ingredients="['Cheese','Wheat','Sugar']"
  >
    <template #notes>
      <p>
        Cheesecake can be flavored in a number of ways.
        The below recipe makes a strawberry cheesecake, but other fruits can be used, fruit can be omitted entirely, or chocolate and/or peanut butter can be added instead.
        Experiment with the mix-ins, but consider that anything with too much liquid will extend the baking time, or cause the cake not to set well in the oven.
      </p>
      </template>
    <template #ingredients>
      <ul>
        <li>3 8oz packages of cream cheese, room temperature</li>
        <li>3 large eggs, room temperature</li>
        <li>3/4 c + 1/3 c sugar</li>
        <li>1 Tbs lemon juice</li>
        <li>2 tsp vanilla</li>
        <li>1/4 tsp salt</li>
        <li>2 graham cracker crusts</li>
        <li>1 lb Strawberries, sliced</li>
      </ul>
    </template>
    <ol>
      <li>Prepare strawberries
        <ol>
          <li>Place sliced strawberries, 1/3 c sugar, and lemon juice in a small saucepan and bring to a simmer over medium high heat</li>
          <li>Simmer until strawberries release liquid, and a sauce begins to form</li>
          <li>Transfer half of strawberries to a blender and puree. Pass the puree through a fine mesh strainer to form a coulis</li>
          <li>Set aside remaining strawberries and refrigerate</li>
        </ol>
      </li>
      <li>Preheat oven to 325˚F</li>
      <li>Mix cream cheese and sugar</li>
      <li>On medium-low speed, mix the eggs in one at a time until just combined</li>
      <li>Add vanilla and salt and mix in</li>
      <li>Divide the mixture between the two pie crusts. Tap them lightly on a table or counter to expel air bubbles</li>
      <li>Gently pour the strawberry coulis over the pie, and stir gently with a knife or toothpick to create a swirl pattern. Take care not to mix the coulis in so much that it becomes homogenous</li>
      <li>Bake the pies for about 40 minutes, until center a toothpick inserted into the center comes out clean. Top may begin to brown a little</li>
      <li>Cool the cheesecakes, then refrigerate for at least 30 minutes. Serve with remaining strawberries</li>
    </ol>
    <template #credits>
      Recipe modified from a holiday cheesecake bars recipe which appeared in a local paper in Wenatchee, WA sometime in 2017.
    </template>
  </RecipeComponent>
</template>