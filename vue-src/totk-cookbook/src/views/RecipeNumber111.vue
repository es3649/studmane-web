<script setup lang="ts">
import RecipeComponent from '@/components/RecipeComponent.vue'
</script>

<template>
    <RecipeComponent name="111: Cheesy Baked Fish" 
        makes="2 Servings"
        :game_ingredients="['Fish','Salmon','Crab','Snail','Cheese']"
    >
        <template #ingredients>
            <ul>
                <li>2 Salmon filets</li>
                <li>4 oz goat cheese</li>
                <li>1/2 tsp dill</li>
                <li>1 lemon (zested and sliced)</li>
                <li>salt and pepper</li>
            </ul>
        </template>
        <ol>
            <li>Preheat oven to 300˚F</li>
            <li>Pat salmon dry with a paper towel. Season with salt and pepper.</li>
            <li>Heat oil in an broiler-safe frying pan (or oven-safe, and transfer to a broiler safe dish before broiling), and place filets skin-side down.</li>
            <li>Sear for 3-5 minutes until browned, then flip and sear the other for 2-3.</li>
            <li>Put the skin side down and transfer pan to oven. Bake for 7-10 minutes, until filet registers 125˚ at the thickest part.</li>
            <li>Prepare cheese mixture: Mix dill, cheese, and lemon zest until combined</li>
            <li>Remove filets from oven and set broiler to 500˚. Gently smear filet tops with cheese mixture and return to oven for 1-2 minutes until cheese is bubbling and begins to brown</li>
            <li>Serve with lemon slices</li>
        </ol>
    </RecipeComponent>
</template>