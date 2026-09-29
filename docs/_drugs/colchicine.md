---
layout: default
title: Colchicine
parent: Evidencia Moderada (L3-L4)
nav_order: 140
evidence_level: L4
indication_count: 3
---

# Colchicine
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **3** 
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

# Colchicina: De Gota a Malaria por Plasmodium falciparum

## Resumen en Una Frase

La colchicina es un alcaloide oral que se usa sobre todo contra la gota y otras enfermedades autoinflamatorias. El registro sanitario colombiano solo indica "COLCHICINA", sin especificar una indicación.
El modelo TxGNN predice que podría ser efectiva para **malaria por Plasmodium falciparum**, pero hoy hay **0 ensayos clínicos** y **6 publicaciones** de laboratorio o serología, ninguna de las cuales evalúa colchicina directamente.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Gota (según la referencia farmacológica); el texto del registro INVIMA solo dice "COLCHICINA" |
| Nueva Indicación Predicha | Malaria por Plasmodium falciparum |
| Puntaje de Predicción TxGNN | 99.60% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

No hay un mecanismo de acción detallado en el paquete de evidencia. Sí se sabe que la colchicina se une a la tubulina (el paquete lista TUBB, tubulina beta clase I, como blanco) y altera los microtúbulos. Por eso interfiere con la división celular y con la actividad de los neutrófilos.

La lógica de la predicción es que algunos compuestos que actúan sobre el citoesqueleto inhiben *P. falciparum* in vitro. Es el caso de los tubulozoles y de la curcumina, que alteró los microtúbulos del parásito. Sin embargo, ninguno de los seis artículos recuperados prueba colchicina. Además, la tubulina de *Plasmodium* se considera poco sensible a la colchicina, y un artículo señala que difiere de la de los mamíferos.

Por lo tanto, el vínculo es indirecto e hipotético. El puntaje alto de TxGNN (0.996) es solo una predicción del modelo y no está respaldado por datos clínicos.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [23505424](https://pubmed.ncbi.nlm.nih.gov/23505424/) | 2013 | In vitro | PloS one | La curcumina altera los microtúbulos de *P. falciparum*; no evalúa colchicina |
| [2655935](https://pubmed.ncbi.nlm.nih.gov/2655935/) | 1989 | In vitro | Cell biology international reports | Sustancias que se unen a tubulina y actina inhiben el parásito in vitro; el tubulozol-T aparece como antimalárico prometedor |
| [2670249](https://pubmed.ncbi.nlm.nih.gov/2670249/) | 1989 | In vitro | Cell biology international reports | Mismo estudio que el anterior (registro duplicado en PubMed) |
| [2221861](https://pubmed.ncbi.nlm.nih.gov/2221861/) | 1990 | In vitro | Antimicrobial agents and chemotherapy | Los tubulozoles reducen la síntesis de proteínas del parásito; la colcemida (análogo de la colchicina) tuvo un efecto similar |
| [7511206](https://pubmed.ncbi.nlm.nih.gov/7511206/) | 1994 | In vitro | Molecular and cellular biology | La expresión del gen pfmdr1 en células de mamífero aumenta la sensibilidad a cloroquina; sin relación directa con colchicina |
| [6362934](https://pubmed.ncbi.nlm.nih.gov/6362934/) | 1984 | Observacional (serología) | Clinical and experimental immunology | El 82% de los pacientes con malaria aguda tenía anticuerpos contra filamentos intermedios del citoesqueleto |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20055858 | COLCHICINA 0.5 MG TABLETAS (Memphis Products S.A.) | Tableta | COLCHICINA |
| 20253882 | SOVUSTA® (Alkem Laboratories Limited) | Tableta | COLCHICINA |

El paquete informa 20 registros en total, pero solo detalla 2 números únicos; el resto aparecen repetidos. Todas las presentaciones son orales.

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: la consulta de interacciones se completó y devolvió 7 registros. En realidad son blancos farmacológicos de la colchicina, no interacciones con otros medicamentos: receptor de glicina α1 y α2, receptor de glicina (todos los subtipos), TAS2R4, TAS2R46, BRD4 y tubulina beta clase I. Todavía no hay un listado de interacciones clínicas (por ejemplo con inhibidores de CYP3A4 o P-gp).

Consultar el prospecto para el resto de la información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia se limita a estudios in vitro con otros compuestos y a una serología, sin ensayos clínicos ni datos con colchicina. La tubulina de *Plasmodium* es poco sensible a la colchicina, y el fármaco tiene un índice terapéutico estrecho. Solo el puntaje del modelo respalda la predicción.

**Para avanzar se necesita:**
- Ensayos in vitro de colchicina contra cultivos de *P. falciparum*, incluidas cepas resistentes a cloroquina, con comparación de toxicidad frente a células humanas
- Obtener el mecanismo de acción completo desde DrugBank
- Descargar y analizar el prospecto de INVIMA para completar advertencias y contraindicaciones
- Un listado real de interacciones farmacológicas, con foco en CYP3A4 y P-gp
- Confirmar la indicación original del fármaco, porque el campo del registro solo repite el nombre

**Nota:** en el mismo paquete, la indicación de rango 2 (fiebre mediterránea familiar) corresponde a un uso ya establecido de la colchicina. Tiene nivel L3 y recomendación "Proceed with Guardrails". No es un hallazgo de reposicionamiento nuevo, y el subtipo "autosómico dominante" debe verificarse frente a la forma recesiva habitual. El rango 3 (dermatofibrosarcoma protuberans) no tiene ninguna evidencia (L5, Hold).

---

*Este informe es solo para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

