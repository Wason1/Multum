select distinct	DNUM = oc1.cki	; select distinct used to prevent duplicate pairs
	, primary_1 = oc1.primary_mnemonic	; returning twice
	, primary_2 = oc2.primary_mnemonic	
		
from	order_catalog oc1	
	, order_catalog oc2	
		
plan	oc1	
where	oc1.catalog_type_cd = 2516	; code value for 'Pharmacy' from code set 6000
and	oc1.cki not in (" ", null, "", "IGNORE")	; exclude "IGNORE" and blank DNUMs
		
join	oc2	
where	oc2.catalog_type_cd = oc1.catalog_type_cd	
and	oc2.cki = oc1.cki	
and	oc2.catalog_cd != oc1.catalog_cd	
		
order by	oc1. primary_mnemonic	
	, 0