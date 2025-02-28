--2c
SELECT comicTitle, issue, publisherName, valuation
FROM Publisher, Comic
WHERE Publisher.publisherID == Comic.publisherID AND valuation > 300 + (SELECT AVG(valuation) FROM Comic);

--2d
SELECT characterName, SUM(valuation) AS [Total Valuation]
FROM Comic, ComicCharacter, CharacterInfo
WHERE Comic.comicID == ComicCharacter.comicID AND ComicCharacter.characterID == CharacterInfo.characterID AND mainCharacter = 1 AND characterName LIKE "%Duck%"
GROUP BY characterName
ORDER BY  SUM(valuation) DESC;

--2e
SELECT comicTitle, issue, publisherName, valuation * 2 AS [Double Price]
FROM Comic, Publisher, Series, CharacterInfo, ComicCharacter
WHERE Series.seriesName = "The OK Seven"
AND characterName == "Starlordly"
AND Comic.publisherID == Publisher.publisherID
AND Comic.seriesID == Series.seriesID
AND Comic.comicID == ComicCharacter.comicID
AND CharacterInfo.characterID == ComicCharacter.characterID;



