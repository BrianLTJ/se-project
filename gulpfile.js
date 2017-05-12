var gulp = require('gulp');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');                //- 压缩js代码

var clean = require('gulp-clean');

const js_files_dev=["./node_modules/vue/dist/vue.js", "./node_modules/jquery/dist/jquery.js", "./node_modules/jquery-json/src/jquery.json.js", "./node_modules/materialize-css/dist/js/materialize.js"];

const js_files_product=["./node_modules/vue/dist/vue.min.js", "./node_modules/jquery/dist/jquery.min.js", "./node_modules/jquery-json/dist/jquery.json.min.js", "./node_modules/materialize-css/dist/js/materialize.min.js"];

gulp.task('clean', function () {
    gulp.src(['./static/lib/js/*','./static/lib/css/*','./rev/*'],{read:false})
        .pipe(clean());
});


gulp.task('compress-js-product',function () {
    gulp.src(js_files_product)
        .pipe(uglify())
        .pipe(concat('lib.js'))
        .pipe(gulp.dest('./static/lib/js'))
        .on('end',function () {
            console.log('compress-js has been completed');
        });
});

gulp.task('compress-js-dev',function () {
    gulp.src(js_files_dev)
        // .pipe(uglify())
        .pipe(concat('lib.js'))
        .pipe(gulp.dest('./static/lib/js'))
        .on('end',function () {
            console.log('compress-js-dev has been completed');
        });
});

gulp.task('default', ['clean','compress-js-product']);

gulp.task('dev', ['clean','compress-js-dev']);

// gulp.task('all', ['clean','compress-js-dev','compress-js-product']);