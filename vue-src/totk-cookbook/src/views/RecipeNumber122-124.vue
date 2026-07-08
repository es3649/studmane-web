<script setup lang="ts">
import SubRecipeComponent from '@/components/SubRecipeComponent.vue'
</script>

<template>
  <h1>122-124: Crêpes</h1>

  <p>
    The in-game crêpes vary only in their toppings, so we provide first the recipe for the plain
    crêpe, then additional notes and directions for the toppings. Crepes can be rolled like taquitos
    to simple eating, or folded in half then again in half or thirds for a fancier look.
  </p>

  <p>
    Crêpes are a vector for all kinds of toppings. Feel free to dress your crêpes in any matter of
    ways. The wildberry and honey crêpe are examples from the game, but I've known crêpes to be
    topped with pudding, whipped cream, Nutella, yogurt, chocolate chips, chocolate sauce, diced
    fruit including strawberries, bananas, pears, blueberries, etc. I've also known crêpes to be
    prepared with savory toppings such as sausage, cured meats, sautéed vegetables in condensed
    cream of chicken soup, ham and cheese, or even topped with Taco Bell hot sauce!
  </p>

  <SubRecipeComponent
    name="122: Plain Crêpe"
    :game_ingredients="['Egg', 'Wheat', 'Milk', 'Butter', 'Sugar']"
    :ingredients="[
      '3 eggs',
      '3/4 c flour',
      '1/2 c water',
      '1/2 c milk',
      '3 Tbs melted butter',
      '1/2 tsp vanilla',
      '1/2 tsp salt',
      'addt\'l butter for greasing the pan',
    ]"
  >
    <ol>
      <li>
        Combine eggs, milk, water, and butter in a blender and beat. Add flour, salt, and vanilla
        and beat until smooth
      </li>
      <li>
        Heat pan and grease liberally with butter. Pour in enough batter to cover the bottom of the
        pan (about 1/4 c for a 9-inch pan). Tilt the pan about to let the batter run around the pan
        and create a thin, homogenous layer.
      </li>
      <li>Cook until brown (about 1 min), then flip and brown the other side.</li>
      <li>
        Repeat this process until batter runs out, re-greasing the pan with butter after each 1-2
        crepes
      </li>
      <li>For the Plain Crêpe, butter the crêpe lightly and sprinkle with sugar</li>
    </ol>
  </SubRecipeComponent>

  <SubRecipeComponent
    name="123: Wildberry Crêpe"
    :game_ingredients="['Egg', 'Wheat', 'Milk', 'Sugar', 'Wildberry']"
    :ingredients="['[Plain Crêpe ingredients]', 'Raspberries', 'Heavy Cream', 'Sugar']"
  >
    <ol>
      <li>Prepare crêpes per the Plain Crêpes recipe</li>
      <li>Whip the Cream...etc.</li>
      <li>Make a Raspberry confit...etc.</li>
    </ol>
  </SubRecipeComponent>

  <SubRecipeComponent
    name="124: Honey Crêpe"
    :game_ingredients="['Egg', 'Wheat', 'Milk', 'Sugar', 'Honey']"
    :ingredients="['[Plain Crêpe ingredients]', 'Honey']"
  >
    <ol>
      <li>Prepare crêpes per the Plain Crêpes recipe</li>
      <li>Top with honey...etc.</li>
    </ol>
  </SubRecipeComponent>

  <h2>Credits</h2>
  <p>Family crêpe recipe</p>
</template>
