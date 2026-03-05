# Write your MySQL query statement below
select sample_id, dna_sequence, species, 
if(dna_sequence like 'ATG%',1,0) as has_start, 
if(dna_sequence like '%TAA' or dna_sequence like '%TAG' or dna_sequence like '%TGA',1,0) as has_stop, 
if(dna_sequence like '%ATAT%',1,0) as has_atat, 
if(dna_sequence like '%GGG%' or dna_sequence like '%GGGG%',1,0) 
as has_ggg from Samples 
group by sample_id 
order by sample_id asc;