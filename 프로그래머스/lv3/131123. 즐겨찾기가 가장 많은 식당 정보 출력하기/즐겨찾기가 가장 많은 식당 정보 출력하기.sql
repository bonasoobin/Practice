select b.FOOD_TYPE,
        b.REST_ID ,
        b.REST_NAME,
        b.FAVORITES
 from (
    select distinct(food_type)
          ,max(favorites) as favorites
    from rest_info 
    group by food_type
) a, rest_info b
where a.food_type=b.food_type
  and a.favorites = b.favorites
order by food_type desc