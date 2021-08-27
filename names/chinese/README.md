## Chinese Name Sources
- [Surnames Wikipedia](https://en.wikipedia.org/wiki/Category:Chinese-language_surnames)
- [Common Surnames](https://en.wikipedia.org/wiki/List_of_common_Chinese_surnames)




### Chinese Surnames Wikidata

```
SELECT ?item ?itemLabel 
WHERE 
{
  ?item wdt:P31 wd:Q1093580.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
```