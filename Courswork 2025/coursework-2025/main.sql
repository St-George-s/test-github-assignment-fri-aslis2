SELECT comicTitle, issue, publisherName, valuation
FROM Publisher, Comic
WHERE Publisher.publisherID == Comic.publisherID AND valuation > 300 + (SELECT AVG(valuation) FROM Comic);


SELECT characterName, SUM(valuation) as [Total Valuation]
FROM Comic, ComicCharacter, CharacterInfo
WHERE Comic.comicID == ComicCharacter.comicID AND ComicCharacter.characterID == CharacterInfo.characterID AND mainCharacter = 1 AND characterName LIKE "%Duck%"
GROUP BY characterName
ORDER BY  SUM(valuation) DESC;


SELECT comicTitle, issue, publisherName, valuation AS [Double Price]
FROM Comic, Publisher, Series, CharacterInfo, ComicCharacter
WHERE Series.seriesName = "The OK Seven"

AND characterName == "Starlordly"

AND Comic.publisherID == Publisher.publisherID

AND Comic.seriesID == Series.seriesID

AND Comic.comicID == ComicCharacter.comicID

AND CharacterInfo.characterID == ComicCharacter.characterID;