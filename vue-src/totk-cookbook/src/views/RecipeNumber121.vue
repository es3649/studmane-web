<script setup lang="ts">
import RecipeComponent from '@/components/RecipeComponent.vue'
</script>
<template>
  <RecipeComponent
    name="121: Egg Pudding"
    makes="6 servings"
    :game_ingredients="['Eggs', 'Milk', 'Sugar']"
  >
    <template #ingredients>
      <ul>
        <li>1/2 c Water</li>
        <li>1 Tbs Light corn syrup</li>
        <li>1/4 tsp Lemon juice</li>
        <li>1 2/3 c Whole Milk</li>
        <li>1 1/3 c Heavy Cream</li>
        <li>3 Large eggs + 2 egg yolks</li>
        <li>1c + 2/3 c Sugar</li>
        <li>1 1/2 tsp Vanilla Extract</li>
        <li>Pinch of Salt</li>
      </ul>
    </template>
    <ol>
      <li>
        Prepare a caramel
        <ol>
          <li>Mix water, corn syrup, and lemon juice in a medium saucepan.</li>
          <li>
            Add 1 c sugar to the saucepan, taking care not to splash sugar on the sides of the pan.
            Stir the sugar gently until it's all moistened.
          </li>
          <li>
            Without stirring, bring the mixture to a boil over medium-high heat until the sugar is
            all dissolved, 6-10 minutes.
          </li>
          <li>
            Reduce heat to medium-low and continue cooking, stirring occasionally, until the mixture
            turns honey-colored.
          </li>
          <li>
            Quickly transfer the liquid evenly to 6 small ramekins. Let the caramel cool in the
            ramekins at least 15 minutes.
          </li>
        </ol>
      </li>
      <li>
        Prepare a custard
        <ol>
          <li>
            Heat milk and cream over medium heat, stirring occasionally, until it begins to steam.
          </li>
          <li>
            In a medium mixing bowl, gently mix eggs and remaining sugar until just combined. Slowly
            and gently whisk in milk mixture, vanilla, and salt
          </li>
          <li>Strain mixture through a fine-mesh strainer</li>
        </ol>
      </li>
      <li>Adjust over rack to middle position, and preheat oven to 350 degrees</li>
      <li>
        Bring a kettle of water to a boil. Place a dish towel in the bottom of a large roasting pan,
        and gently pour the boiling water over the towel.
      </li>
      <li>
        Arrange the caramel ramekins on the towel in the boiling water. Distribute the custard
        mixture evenly between the Ramekins.
      </li>
      <li>
        Bake until a paring knife inserted halfway between the center and the rim of the ramekins
        comes out clean, about 35-40 min.
      </li>
      <li>Transfer ramekins to a wire rick to cool before serving.</li>
      <li>
        To serve, slide a paring knife around the rim of hte ramekin to unstick the custard from the
        vessel. Place a small plate over the top of the ramekin, then invert. Carefully remove the
        ramekin so that the inverted pudding is left on the plate, gently shaking ramekin as needed
        to dislodge the pudding.
      </li>
    </ol>
    <template #credits>
      <p>
        Recipe adapted from America's Test Kitchen Cooking School Cookbook recipe for Crème Caramel
      </p>
    </template>
  </RecipeComponent>
</template>
