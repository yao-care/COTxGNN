---
layout: default
title: Lactic Acid
parent: Solo Predicción del Modelo (L5)
nav_order: 371
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Lactic Acid: nueva indicación predicha, Coartacion atipica de la aorta (nivel de evidencia L5). Indicación original: Paracetamol, combinaciones excluyendo sicolepticos"
---

# Lactic Acid
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Ácido láctico: De Combinaciones de Paracetamol a Coartación Atípica de la Aorta

## Resumen en Una Frase

El registro sanitario colombiano disponible para este farmaco corresponde a una combinacion de paracetamol (acetaminofen + naproxeno), cuya categoria de indicacion es "Paracetamol, combinaciones excluyendo sicolepticos".
El modelo TxGNN predice que el acido lactico podria ser efectivo para **coartacion atipica de la aorta**, pero **no hay ensayos clinicos ni publicaciones** que respalden esta direccion.
Se trata de una prediccion puramente computacional (nivel de evidencia L5).

---

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Paracetamol, combinaciones excluyendo sicolepticos |
| Nueva Indicacion Predicha | Coartacion atipica de la aorta |
| Puntaje de Prediccion TxGNN | 99.59% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Numero de Registros Sanitarios | 1 (cancelado) |
| Decision Recomendada | Hold |

---

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de accion. El unico registro sanitario asociado en Colombia corresponde a una capsula blanda que combina acetaminofen 325 mg y naproxeno 220 mg, por lo que la indicacion original registrada no refleja el uso habitual del acido lactico como tal (un metabolito comun y agente regulador de pH).

Los datos compilados para este informe no respaldan un vinculo mecanistico. La coartacion de la aorta es un defecto vascular estructural y no hay indicios de que el acido lactico pueda corregirlo. El puntaje del modelo es muy alto (99.59%), pero es solo una prediccion computacional sin ensayos ni literatura que la sustenten.

Por ello, esta prediccion debe considerarse una hipotesis sin fundamento mecanistico demostrado.

### Otras predicciones del modelo (todas de nivel L5, decision Hold)

| Posicion | Indicacion predicha | Puntaje TxGNN | Ensayos | Publicaciones | Comentario |
|------|------|------|------|------|------|
| 2 | Malformacion aortica | 99.35% | 0 | 14 | La literatura solo tiene relacion de palabras clave (cirugia cardiaca congenita, dispositivos biodegradables, lactato como marcador de perfusion); ninguna evalua el acido lactico como terapia |
| 3 | Malformacion esofagica no sindromica | 99.23% | 0 | 0 | Defecto del desarrollo de tratamiento quirurgico; sin papel farmacologico plausible |
| 4 | Amenorrea | 99.16% | 0 | 1 | Un estudio observacional en babuinos sobre microbiota vaginal; no demuestra efecto terapeutico |
| 5 | Sindrome de ojo seco | 99.13% | 0 | 6 | Ningun estudio prueba el acido lactico como tratamiento; los acidos topicos podrian irritar la superficie ocular |

---

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clinicos relacionados registrados.

---

## Evidencia de Literatura

Para la indicacion principal (coartacion atipica de la aorta) no hay literatura relacionada disponible. A modo de referencia, la segunda prediccion (malformacion aortica) tiene publicaciones recuperadas, aunque solo guardan relacion por palabras clave:

| PMID | Ano | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [23791497](https://pubmed.ncbi.nlm.nih.gov/23791497/) | 2013 | ECA | J Cardiothorac Vasc Anesth | Estrategia combinada de ultrafiltracion en cirugia cardiaca pediatrica; no evalua acido lactico |
| [3367436](https://pubmed.ncbi.nlm.nih.gov/3367436/) | 1988 | Preclinico (animal) | J Vasc Surg | Metabolismo de la pared aortica y aterosclerosis en conejos con coartacion |
| [25157439](https://pubmed.ncbi.nlm.nih.gov/25157439/) | 2015 | Preclinico (animal) | Catheter Cardiovasc Interv | Stent biodegradable de acido poli-L-lactico en aorta descendente de conejo |
| [31714687](https://pubmed.ncbi.nlm.nih.gov/31714687/) | 2020 | Serie de casos | Catheter Cardiovasc Interv | Dispositivo biodegradable de PLLA para cierre de comunicacion interauricular |
| [32382764](https://pubmed.ncbi.nlm.nih.gov/32382764/) | 2020 | Reporte de casos | Pediatr Cardiol | Microplacas absorbibles de PLLA para broncomalacia en cardiopatia congenita |

Estos estudios usan acido poli-L-lactico como material de dispositivos o el lactato como marcador, no como tratamiento farmacologico.

---

## Informacion de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmaceutica | Indicacion Aprobada |
|---------|------|------|-----------|
| 20167956 (cancelado) | ACETAMINOFEN 325 MG + NAPROXENO 220MG | Capsula blanda | Paracetamol, combinaciones excluyendo sicolepticos |

---

## Consideraciones de Seguridad

**Interacciones Farmacologicas:** se identificaron 17 interacciones, todas de nivel moderado o leve.

- **Moderadas (10):** doxiciclina, acido acetilsalicilico, tetraciclina, minociclina, efedrina, efedrina (nasal), pseudoefedrina, demeclociclina, oxitetraciclina y salicilato de sodio.
- **Leves (7):** clorpropamida, tolazamida, glipizida, gliburida, acetohexamida, tolbutamida y metotrexato.

No se dispone de datos de advertencias ni contraindicaciones del prospecto. Consultar el prospecto para informacion adicional de seguridad.

---

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
La prediccion tiene un puntaje alto, pero no cuenta con ensayos clinicos ni literatura que evalue el acido lactico como terapia, y no existe un vinculo mecanistico plausible con una malformacion vascular estructural. Ademas, el unico registro sanitario en Colombia esta cancelado y corresponde a una combinacion distinta.

**Para avanzar se necesita:**
- Datos del mecanismo de accion (por ejemplo, desde DrugBank)
- Prospecto con advertencias y contraindicaciones (INVIMA)
- Aclarar la discrepancia entre el farmaco (acido lactico) y el producto registrado (acetaminofen + naproxeno)
- Evidencia preclinica o mecanistica que sustente un papel del acido lactico en la indicacion predicha
- Evaluar si alguna de las otras predicciones (por ejemplo, ojo seco) tiene una base biologica mas plausible, con revision previa de seguridad
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

