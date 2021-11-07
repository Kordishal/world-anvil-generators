### Mythical Creatures Inspiration

A big list of all the mythical creatures represented on Wikipedia. Needs some curation.
The idea is to be able to roll this table when I need inspiration for a creature to write about them.


#### ToDo

* Add descriptions for each creature
* Add labels for the languages not available.
* Add links directly to Wikipedia
* Add more creatures.
* Add categories for creature types.
* Add tags for creatures.


#### Sources

Wikipedia offers a great list of Mythical Creatures from all over the world. These 
creatures can be a great source of inspiration for world building.

* [Mythical Creature](https://www.wikidata.org/wiki/Q2239243)


```sparksql
SELECT DISTINCT ?mythicalCreature ?mythicalCreatureLabel ?mythicalCreatureDescription
WHERE
{
  ?mythicalCreature wdt:P31/wdt:P279* wd:Q2239243 . 
  SERVICE wikibase:label { #BabelRainbow
    bd:serviceParam wikibase:language "[AUTO_LANGUAGE],fr,ar,be,bg,bn,ca,cs,da,de,el,en,es,et,fa,fi,he,hi,hu,hy,id,it,ja,jv,ko,nb,nl,eo,pa,pl,pt,ro,ru,sh,sk,sr,sv,sw,te,th,tr,uk,yue,vec,vi,zh"
  }
  #FILTER(NOT EXISTS {
  #  ?mythicalCreature schema:description ?mythicalCreatureDescription.
  #  FILTER(LANG(?mythicalCreatureDescription) = "en")
  # })
  ?mythicalCreature schema:description ?mythicalCreatureDescription.
  FILTER(LANG(?mythicalCreatureDescription) = "en")
}
ORDER BY ?mythicalCreatureLabel
```

