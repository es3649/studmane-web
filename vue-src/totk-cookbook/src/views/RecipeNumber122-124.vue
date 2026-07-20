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
    id="plain-crepes"
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
    :ingredients="[
      'Plain Crêpes',
      '6 oz Raspberries',
      'Whipped Cream',
      '2 Tbs Sugar',
      '1/2 tsp Lemon juice or water',
    ]"
  >
    <template #ingredients>
      <ul>
        <li>6 oz fresh raspberries</li>
        <li>2 Tbs Sugar</li>
        <li>1/2 tsp lemon juice, lime juice, or water</li>
      </ul>
    </template>
    <ol>
      <li>
        Prepare a Raspberry Coulis

        <ol>
          <li>
            Place berries, 2 Tbs sugar and lime juice or water in a small saucepan and simmer over
            medium-high heat until the the mixture is boiling
          </li>
          <li>And cornstarch and continue to stir for</li>
          <li>Puree berries with blender until smooth</li>
          <li>
            Pass the mixture through a fine mesh strainer to remove seeds. Press it through with a
            spatula to get as much coulis as possible.
          </li>
          <li>Cool before serving.</li>
        </ol>
      </li>

      <li>Prepare crêpes per the <a href="#plain-crepes">Plain Crêpes recipe</a></li>
      <li>Top the crêpe with whipped cream and raspberry coulis</li>
    </ol>
  </SubRecipeComponent>

  <SubRecipeComponent
    name="124: Honey Crêpe"
    :game_ingredients="['Egg', 'Wheat', 'Milk', 'Sugar', 'Honey']"
    :ingredients="['Plain Crêpes', 'Butter', 'Honey']"
  >
    <template #notes>
      Frankly, I thing there are mre interesting ways to enjoy crepes, but this is one of the ways
      Link eats them, so it's worth it at least for that.
    </template>
    <ol>
      <li>Prepare crêpes per the <a href="#plain-crepes">Plain Crêpes recipe</a></li>
      <li>Butter the warm crêpe and drizzle with honey</li>
    </ol>
  </SubRecipeComponent>

  <h2>Credits</h2>
  <p>Family crêpe recipe</p>
</template>
