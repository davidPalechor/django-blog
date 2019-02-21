var gulp = require('gulp')
var sass = require('gulp-sass')

gulp.task('sass', function(){
    return gulp.src('app/static/sass/style.sass')
        .pipe(sass())
        .pipe(gulp.dest('app/static/css'))
})

gulp.task('default', gulp.parallel("sass"))