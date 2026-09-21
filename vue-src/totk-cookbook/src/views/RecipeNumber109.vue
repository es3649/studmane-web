<script setup lang="ts">
import RecipeComponent from '@/components/RecipeComponent.vue';
</script>
<template>
    <RecipeComponent 
        name="109 Fish Pie" 
        makes=""
        :game_ingredients="['Fish','Salmon','Wheat','Butter','Salt']"
    >
    <ol>
        <li><b>Prepare a crust</b>
            <ol>
                <li>Sift Flour and salt together in a medium bowl</li>
                <li>Make a well in the middle and add water and egg yolks</li>
                <li>Add butter, and mix with a fork until chinky dough is formed</li>
                <li>Continue to work the dough by hand until mostly combined. A few buttery chunks are ok</li>
                <li>Roll dough into a ball, and refrigerate</li>
            </ol>
        </li>
        <li><b>Prepare the salmon filet</b>
            <ol>
                <li>Pat dry with a paper towel and season with salt and pepper</li>
                <li>Preheat oven to 300˚F</li>
                <li>Heat olive oil in a medium, oven-safe frying pan</li>
                <li>Sear salmon skin-side down until browned, about 3 minutes</li>
                <li>Gently flip over, and sear the top side, about 3 minutes</li>
                <li>Flop skin-side back down, transfer pan to the oven, and bake until the inside of the filet reaches 125˚F, 7-10 minutes</li>
                <li>Remove filet from oven and cool, then shred. Adjust oven temperature to 425˚F</li>
                <li>Once salmon is cool, remove the skin, and gently mash the salmon with a fork. Gently cut apart any part of the seared top which doesn't flake easily</li>
            </ol>
        </li>
        <li>Steam the onions, carrots, celery, and leeks for 5 minutes. (If vegetables are prepared before the salmon is in the oven, this can be done while the salmon is baking.)</li>
        <li>Roll out the dough on a floured surface to about 1/4 inch thick. Lay 10-inch pie dish down upside down on top of the rolled out dough to be sure the size is correct</li>
        <li>
            <b>Prepare the filling</b>
            <ol>
                <li>Melt butter in medium saucepan. Whisk in flour until smooth</li>
                <li>Stir in broth and milk, and cook until thickened, a minute or two</li>
                <li>Add salt, and lemon zest and cook for a minute longer, then add steamed vegetables, cauliflower rice, and macerated salmon and stir until just combined</li>
            </ol>
        </li>
        <li>Pour the filling into the pie dish, then top with the crust. Bake at 425˚F for 30 minutes</li>
    </ol>
    <template #ingredients>
        <h3>Crust</h3>
        <ul>
            <li>1 1/2c flour</li>
            <li>1/2 tsp Salt</li>
            <li>3 Tbs ice water</li>
            <li>2 egg yolks</li>
            <li>2/3c butter</li>
        </ul>
        <h3>Filling</h3>
        <ul>
            <li>1lb salmon filet, skin on</li>
            <li>2 carrots, chopped</li>
            <li>3 celery stalks, chopped</li>
            <li>1 onion, chopped</li>
            <li>1 leek, roots and greens removed, halved, and sliced</li>
            <li>1c cauliflower rice</li>
            <li>4 Tbs butter</li>
            <li>5 Tbs flour</li>
            <li>1 1/2c Chicken broth</li>
            <li>2/3c milk</li>
            <li>1 tsp lemon zest</li>
            <li>1/2 tsp salt</li>
            <li>Pepper</li>
        </ul>
    </template>
    </RecipeComponent>
</template>