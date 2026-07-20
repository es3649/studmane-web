<script setup lang="ts">
import RecipeComponent from '@/components/RecipeComponent.vue'
</script>
<template>
  <RecipeComponent
    name="38: Pepper Seafood"
    makes="4 servings"
    :game_ingredients="['Fish/Salmon/Crab', 'Hot Peppers']"
  >
    <div>
      <h3>Puréed Jalapeño Confit</h3>
      <ol>
        <li>Chop peppers into 1-inch pieces</li>
        <li>
          Place peppers and garlic into a small in a small saucepan, and submerge in oil. Cook on
          low for 1 hour.
        </li>
        <li>Drain off oil, reserving 1 Tbs</li>
        <li>
          Place peppers, garlic, reserved oil, and salt in blender. Pulse a few times to break up
          the larger pieces, then blend until smooth.
        </li>
      </ol>
      <h3>Roasted Salmon Filets</h3>
      <ol>
        <li>
          Place oven rack on lowest setting, and put rimmed baking sheet in the oven. Preheat oven
          to 500°F
        </li>
        <li>
          If the filet has skin on, make 4-5 slits along the back of the filet, cutting through the
          skin, but avoiding the flesh beneath
        </li>
        <li>
          Pat the filet dry with a paper towel. Lather evenly evenly with the oil, then season with
          salt and pepper.
        </li>
        <li>
          Remove the baking sheet from the oven, and reduce oven temperature to 275°F. Place the
          filet on the heated sheet, and return it to the oven. Bake for 8-13 minutes, until the
          meat in the center of the filet is just translucent.
        </li>
        <li>Cut the filet into 4 evenly-sized pieces, and top with pepper sauce.</li>
      </ol>
    </div>
    <template #ingredients>
      <h3>Sauce</h3>
      <ul>
        <li>5 jalapeño peppers</li>
        <li>3-4 cloves of garlic</li>
        <li>1 1/2 c olive oil</li>
        <li>1/4 tsp salt</li>
      </ul>
      <h3>Salmon</h3>
      <ul>
        <li>1 1.5-2 lb salmon filet</li>
        <li>2 Tbs olive oil</li>
        <li>Salt and pepper</li>
      </ul>
    </template>
    <template #credits>
      <p>Roasted Salmon recipe summarized from America's Test Kitchen Cooking School Cookbook.</p>
    </template>
  </RecipeComponent>
</template>
