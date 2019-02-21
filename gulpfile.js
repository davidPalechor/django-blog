var gulp = require('gulp')
var sass = require('sass')

gulp.task('sass', function(){
    return gulp.src('app/static/sass/style.sass')
        .pipe(sass())
        .pipe(gulp.dest('app/static/css'))
})

gulp.task('default', ["sass"])