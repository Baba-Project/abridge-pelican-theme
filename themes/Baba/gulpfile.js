import * as sass from "sass";
import gulpSass from "gulp-sass";
import gulp from "gulp";
import cleanCSS from "gulp-clean-css";
import sourcemaps from "gulp-sourcemaps";
import uglify from "gulp-uglify";
import rename from "gulp-rename";
import plumber from "gulp-plumber";
import cache from "gulp-cache";

const sassCompiler = gulpSass(sass);

// SCSS'i CSS'e Dönüştür ve Minify Et
gulp.task("sass", function () {
  return gulp
    .src("static/scss/style.scss")
    .pipe(plumber()) // Hata işleme
    .pipe(sourcemaps.init())
    .pipe(sassCompiler().on("error", sassCompiler.logError))
    .pipe(cleanCSS())
    .pipe(sourcemaps.write("."))
    .pipe(gulp.dest("static/css"));
});

// JavaScript'i Minify Et
gulp.task("js", function () {
  return gulp
    .src("static/js/main.js")
    .pipe(plumber()) // Hata işleme
    .pipe(sourcemaps.init())
    .pipe(uglify())
    .pipe(rename("theme.min.js"))
    .pipe(sourcemaps.write("."))
    .pipe(gulp.dest("static/js"));
});

// SCSS ve JavaScript Dosyalarını İzle
gulp.task("watch", function () {
  gulp.watch(
    ["static/scss/**/*.scss", "!static/scss/**/*.map"],
    gulp.series("sass"),
  );
  gulp.watch(
    ["static/js/**/*.js", "!static/js/**/*.map", "!static/js/theme.min.js"],
    gulp.series("js"),
  );
});

// Varsayılan Görev
gulp.task("default", gulp.series("sass", "js", "watch"));
