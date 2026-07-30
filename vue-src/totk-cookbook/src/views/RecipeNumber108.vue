<script setup lang="ts">
import RecipeComponent from '@/components/RecipeComponent.vue'
</script>
<template>
  <RecipeComponent
    name="108: Meat Pie"
    makes="about 9 pies"
    :game_ingredients="['Meat', 'Poultry', 'Wheat', 'Butter', 'Salt']"
  >
    <template #ingredients>
      <ul>
        <li>3/4 lb Eye of Round (Chuck) steak</li>
        <li>4 crimini or white mushrooms</li>
        <li>1 medium onion</li>
        <li>3 Tbs oil</li>
        <li>1.5 c red wine</li>
        <li>Salt and Pepper</li>
        <li>2 c + 2 Tbs flour</li>
        <li>2/3 c + 2 Tbs shortening (or room temperature butter)</li>
        <li>1/2 tsp salt</li>
        <li>1/4 c + 4-6 Tbs cold water</li>
      </ul>
    </template>
    <ol>
      <li>
        Prepare a <b>filling</b>
        <ol>
          <li>Salt and pepper the chopped steak</li>
          <li>Sauté mushrooms in 1/4c water until liquid evaporates</li>
          <li>Add 1 Tbs oil an onions and sauté</li>
          <li>
            Once onions and mushrooms are nearly finished, heat 2 Tbs of oil in a separate pan and
            sear steak quickly
          </li>
          <li>
            Transfer onions and mushrooms to the steak pan, then add 2 Tbs flour. Cook for one
            minute
          </li>
          <li>Deglaze the pan with wine, stirring until flour mixed into the wine</li>
          <li>Simmer until gravy is thick and no longer smells of alcohol</li>
        </ol>
      </li>
      <li>
        Prepare a <b>pie crust</b>
        <ol>
          <li>Mix flour and salt in a large bowl</li>
          <li>Cut in shortening with two knives until the pieces are about pea-sized</li>
          <li>
            Add 4 Tbs water, and stir in with a fork. Add remaining water 1 Tbs at a time until
            dough forms up in large chunks
          </li>
        </ol>
      </li>
      <li>
        Form the dough into a ball, and roll out tou about 1/8 inch on a lightly floured surface.
        Cut out circles about 4-3/4 inches in diameter for the bottoms, and about 3 inches in
        diameter for the tops
      </li>
      <li>
        Form the larger rounds into the bottom of a muffin tin so that they sit flat on the bottom.
        Press the dough up the sides to form a uniform thickness. Leave a little dough poking over
        the top to pinch the pastries closed. Press addition dough scraps into the bottom or sides
        to fill in any holes/thin spaces.
      </li>
      <li>Fill the pie shells about to the brim with the filling</li>
      <li>Place a 3 inch round atop the filled pie shell and pinch around the rim to close</li>
      <li>
        Cut one or two short slits on the top of the pie for decoration, and to allow the filling to
        expand without breaking the seal around the edge
      </li>
      <li>Bake at 425˚F for 22-25 minutes, until tops of the pies are browned</li>
    </ol>
    <template #credits>
      <p>Pie crust from Betty Crocker</p>
    </template>
  </RecipeComponent>
</template>
