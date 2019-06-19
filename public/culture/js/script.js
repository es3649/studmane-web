const imgList = ["buenos-aires.JPG", "cusco.JPG", "machu-picchu.JPG", "vina-del-mar.JPG", "cusco-flowers.JPG", "santiago.JPG"];

var app = new Vue({
    el: "#root",

    data: {
        ideology: false,
        motherland: false,
        natives: false,
    },
    
    computed: {
        image: () => {
            let rand = Math.round(Math.random() * imgList.length);
            if (rand >= imgList.length) {
                rand = 0;
            }
             let image = "'css/res/" + imgList[rand] + "'";
            console.log("using background", rand + ":", image);
            return image;
        },
    },
    
    methods: {
        showIdeology() { this.ideology = !this.ideology; },
        showMotherland() { this.motherland = !this.motherland; },
        showNatives() { this.natives = !this.natives; },
    },
})