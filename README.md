# stack overflow tag analysis

This project fetches StackOverflow API get questions and make tag analysis

# install

pip install sosq

pip install emek

# for use

1- Get your key and token from stackexchange (https://stackapps.com/users/login?returnurl=/apps/oauth/register)

2- sample code below.

```
import sosq
import emek
df = sosq.get_result("your_search_query", "your_key", "your_access_token")
emek.process_data(df)
```

