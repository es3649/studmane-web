<script setup lang="ts">
import RecipeComponent from '@/components/RecipeComponent.vue';
</script>

<template>
<RecipeComponent name="94-96: Meat and Rice Bowl" 
  makes="4 servings"
  :game_ingredients="['Meat','Poultry','Rice','Salt']">
  <template #ingredients>
      <ul>
      <li>1 1lb steak, about 1-in thick</li>
      <li>1 Tbs oil</li>
      <li>Salt and pepper</li>
      <li>4 c cooked rice</li>
      <li>1 shallot, minced</li>
      <li>2-3 cloves garlic, minced</li>
      <li>2 Tbs red wine vinegar</li>
      <li>1 c chicken broth</li>
      <li>3 Tbs butter</li>
      <li>Pepper</li>
    </ul>
  </template>
  <ol>
    <li><b>Prepare Steak</b>
      <ol>
        <li>Pat steak sry with paper towel, then season both sides with salt and pepper</li>
        <li>Heat 1 Tbs oil in frying pan over medium-high heat. Sear one side of steak until browned, 3-4 minutes</li>
        <li>Flip steak and continue to cook until the inside reaches 115-120˚F (rare) or 120-125˚F (medium rare)</li>
        <li>Remove steak from pan and rest for about 10 minutes</li>
      </ol>
    </li>
    <li><b>Sauce</b>
      <ol>
        <li>Sauté shallot in the remaining fat in the steak pan, scraping up the fond left by the steak while they cook</li>
        <li>Add garlic and sauté until fragrant, about 30 seconds</li>
        <li>Add vinegar and broth and scrape up any remaining brown bits in the pan</li>
        <li>Add butter and season with pepper</li>
        <li>Cook until the sauce has reduced to a thin-gravy-like texture</li>
      </ol>
    </li>
    <li>Chop rested steak into strips, and stir any released juices into the pan sauce. If strips are too long, cut them in halves or thirds</li>
    <li>Serve strips over rice and top with sauce</li>
  </ol>
</RecipeComponent>
</template>