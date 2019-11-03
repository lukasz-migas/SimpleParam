# SimpleParam

## Badges

[![Build Status](https://travis-ci.com/lukasz-migas/SimpleParam.svg?branch=master)](https://travis-ci.com/lukasz-migas/SimpleParam)
[![CircleCI](https://circleci.com/gh/lukasz-migas/SimpleParam.svg?style=svg)](https://circleci.com/gh/lukasz-migas/SimpleParam)
[![Build status](https://ci.appveyor.com/api/projects/status/518hbck32eaekp4w?svg=true)](https://ci.appveyor.com/project/lukasz-migas/simpleparam)
[![codecov](https://codecov.io/gh/lukasz-migas/SimpleParam/branch/master/graph/badge.svg)](https://codecov.io/gh/lukasz-migas/SimpleParam)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/775f9aedd36b49de9400362fe3a57918)](https://www.codacy.com/manual/lukasz-migas/SimpleParam?utm_source=github.com&utm_medium=referral&utm_content=lukasz-migas/SimpleParam&utm_campaign=Badge_Grade)
[![CodeFactor](https://www.codefactor.io/repository/github/lukasz-migas/simpleparam/badge)](https://www.codefactor.io/repository/github/lukasz-migas/simpleparam)

## About

`SimpleParam` was inspired by the [param](https://param.pyviz.org/) library which offers lots of neat features in a
small package, however `param` has a tricky codebase. In `SimpleParam` you can either create `Parameter` or
`ParameterStore` using simple synthax.

`SimpleParam` is certainly not complete and is missing a lot of awesome features of `param` and of course, has not been battle-tested yet. Missing features (such as `Array`, `List`, etc) will be added as my other projects that use `SimpleParam` will require them.

## Features

`SimpleParam` has a couple of useful features that should simplify creation of configuration classes

-   multiple built-in classes `Number`, `Integer`, `Range`, `Boolean`, `String`, `Color` and `Choice`
-   automated type checking (e.g. `Number`, `Integer`, `String`, `Boolean`)
-   automated range checking (e.g.`Number`, `Integer`, `Range`)
-   automated choice checking (e.g. `Choice`)
-   when bundled together in a `ParameterStore`, values can be easily protected (set `constant=True`) or exported (set `saveable=True`)
