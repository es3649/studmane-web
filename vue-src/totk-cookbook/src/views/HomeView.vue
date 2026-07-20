<script setup lang="ts">
import { RouterLink } from 'vue-router'
import { computed, ref } from 'vue'
import { MEALS, type Meal } from '@/data'
import { DESSERT, ENTREE, SIDE, SOUP } from '@/meal_category'
import { ALL_INGREDIENTS, type Ingredient } from '@/ingredients'
import Multiselect from 'vue-multiselect'

const group = ref<boolean>(true)
const sort = ref<string>('number')
const selected_ingredients = ref<Ingredient[] | null>([])

const id_sorter = (a: Meal, b: Meal) => {
  return a.id - b.id
}

const name_sorter = (a: Meal, b: Meal) => {
  if (a.name < b.name) {
    return -1
  } else if (a.name > b.name) {
    return 1
  }
  return 0
}

const matching = computed(() =>
  MEALS.filter((meal) =>
    selected_ingredients.value?.every((ingredient) => meal.ingredients.includes(ingredient)),
  ).sort(sort.value == 'name' ? name_sorter : id_sorter),
)

const entrees = computed(() =>
  MEALS.filter(
    (meal) =>
      meal.category == ENTREE &&
      selected_ingredients.value?.every((ingredient) => meal.ingredients.includes(ingredient)),
  ).sort(sort.value == 'name' ? name_sorter : id_sorter),
)

const soups = computed(() =>
  MEALS.filter(
    (meal) =>
      meal.category == SOUP &&
      selected_ingredients.value?.every((ingredient) => meal.ingredients.includes(ingredient)),
  ).sort(sort.value == 'name' ? name_sorter : id_sorter),
)

const sides = computed(() =>
  MEALS.filter(
    (meal) =>
      meal.category == SIDE &&
      selected_ingredients.value?.every((ingredient) => meal.ingredients.includes(ingredient)),
  ).sort(sort.value == 'name' ? name_sorter : id_sorter),
)

const desserts = computed(() =>
  MEALS.filter(
    (meal) =>
      meal.category == DESSERT &&
      selected_ingredients.value?.every((ingredient) => meal.ingredients.includes(ingredient)),
  ).sort(sort.value == 'name' ? name_sorter : id_sorter),
)
</script>

<template>
  <h1>TotK Cookbook</h1>
  <div>
    <p>
      This is a fun little project I'm working on to find or create recipes for many of the dishes
      the player can cook in Legend of Zelda: Tears of the Kingdom.
    </p>
    <img src="@/res/totk-logo.png" class="totk-logo" />

    <p>
      I've left out a few recipes which seemed uninteresting&mdash;like roasted individual mushroom
      species or simmered tomatoes&mdash;as well as recipes which are nonsense in the real
      world&mdash;like monstrous food, dark food, and elixirs. I've also collapsed several recipes
      together. In cases of recipes like the risottos or crêpes, this is mostly because the change
      in ingredients is pretty close to just that. In other cases, it's because the in-game recipes
      differentiate between meat, prime meat, and gourmet meat. If you'd like to respect that
      distinction in your cooking, choose a more expensive cut of meat, or use USDA Prime.
    </p>

    <p>
      The general rule for these recipes is that they must use the same ingredients that they do in
      Legend of Zelda: Tears of the Kingdom. Obviously, some allowances have to be made since I
      can't find Voltfruit in real life (though maybe I'll use dragonfruit instead), but most
      ingredients correspond pretty closely with real-life foods. I did allow some embellishment
      with other ingredients to make each dish more well-rounded and flavorful, and in some cases to
      make them possible (wheat bread with only wheat and salt? Please.)
    </p>

    <p>
      Lastly, I can't guarantee that any of these recipes will increase your attack power or
      stealth, but most of them should replenish your hearts, and maybe even stamina. For legal
      reasons, I can't recommend throwing yourself at enemies over and over to no avail, even if you
      are cooking special dishes and elixirs.
    </p>
  </div>

  <h2>Recipe Book</h2>

  <div class="button-box">
    <p>
      Sort by:
      <input id="name_sort" type="radio" value="name" v-model="sort" />
      <label for="name_sort">name</label>
      &nbsp;
      <input id="number_sort" type="radio" value="number" v-model="sort" />
      <label for="number_sort">number</label>
      <br />
      <label for="group">Group by Course:</label>
      &nbsp;
      <input id="group" type="checkbox" v-model="group" />
      <br />
      Search In-Game Ingredients:
      <br />
      <!-- <select v-model="selected_ingredients" placeholder="Ingredients" multiple>
        <option v-for="item of ALL_INGREDIENTS" :key="item">{{ item }}</option>
      </select> -->
      <Multiselect
        id="ingredient-selector"
        v-model="selected_ingredients"
        :options="ALL_INGREDIENTS"
        :multiple="true"
        :close-on-select="false"
        :clear-on-select="false"
        :taggable="true"
        @tag="() => {}"
      />
    </p>
  </div>

  <div v-if="group">
    <h3>Entrées</h3>
    <p v-if="entrees.length == 0"><i>No matching entrées</i></p>
    <ul>
      <li v-for="value in entrees" v-bind:key="value.id">
        <RouterLink :to="`/${value.numbers}`">{{ value.numbers }}: {{ value.name }}</RouterLink>
      </li>
      <!-- <li>
        <RouterLink to="./80-84"
          >80-84: Risottos (Vegetable, Mushroom, Salmon, Crab, Cheese)</RouterLink
        >
      </li> -->
    </ul>

    <h3>Soups</h3>
    <p v-if="soups.length == 0"><i>No matching soups</i></p>
    <ul>
      <li v-for="value in soups" v-bind:key="value.id">
        <RouterLink :to="`/${value.numbers}`">{{ value.numbers }}: {{ value.name }}</RouterLink>
      </li>
    </ul>

    <h3>Sides/Starters</h3>
    <p v-if="sides.length == 0"><i>No matching sides/starters</i></p>
    <ul>
      <li v-for="value in sides" v-bind:key="value.id">
        <RouterLink :to="`/${value.numbers}`">{{ value.numbers }}: {{ value.name }}</RouterLink>
      </li>
    </ul>

    <h3>Desserts</h3>
    <p v-if="desserts.length == 0"><i>No matching desserts</i></p>
    <ul>
      <li v-for="value in desserts" v-bind:key="value.id">
        <RouterLink :to="`/${value.numbers}`">{{ value.numbers }}: {{ value.name }}</RouterLink>
      </li>
    </ul>
  </div>
  <div v-else>
    <h3>All Dishes</h3>
    <p v-if="matching.length == 0"><i>No matching meals</i></p>
    <ul>
      <li v-for="value in matching" v-bind:key="value.id">
        <RouterLink :to="`/${value.numbers}`">{{ value.numbers }}: {{ value.name }}</RouterLink>
      </li>
    </ul>
  </div>

  <h4>Credits</h4>
  <p><a href="https://artsyomni.com/hyliaserif">Hylia Serif</a> font by Artsy Omni</p>
  <p>
    <i>
      Disclaimer: This project is not affiliated with nor endorsed by Nintendo. The Legend of Zelda
      is a registered trademark of Nintendo of America Inc.
    </i>
  </p>
</template>

<style lang="css" scoped>
.button-box label,
.button-box input {
  display: inline-block;
}
</style>
