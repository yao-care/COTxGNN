---
layout: default
title: Darunavir
parent: 僅模型預測 (L5)
nav_order: 94
evidence_level: L5
indication_count: 4
---

# Darunavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Darunavir: De Infección por VIH-1 a Síndrome de Inmunodeficiencia Adquirida Felina

## Resumen en Una Frase

Darunavir es un inhibidor de proteasa diseñado específicamente contra el VIH-1, aprobado internacionalmente como componente de la terapia antirretroviral combinada en adultos y pacientes pediátricos. El modelo TxGNN predice que podría ser efectivo para el **Síndrome de Inmunodeficiencia Adquirida Felina (FIV)**, aunque actualmente **no existen ensayos clínicos relevantes ni publicaciones científicas** que respalden directamente esta indicación. La predicción parece derivar de una asociación taxonómica superficial entre lentivirus, pero carece completamente de respaldo experimental específico para la proteasa del FIV.

---

## Resumen Rápido

| Ítem | Contenido |
|------|------|
| Indicación Original | Infección por VIH-1 (terapia antirretroviral combinada) |
| Nueva Indicación Predicha | Síndrome de inmunodeficiencia adquirida felina |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la fuente de datos consultada. Según la información conocida, Darunavir es un inhibidor de proteasa del VIH-1 que bloquea el sitio activo de la enzima proteasa viral, impidiendo la escisión de precursores poliproteicos y, por ende, la maduración de nuevas partículas virales infecciosas. Su eficacia en el tratamiento del VIH-1 ha sido ampliamente validada en ensayos clínicos de fase 3 y en práctica clínica real durante más de una década.

La predicción del modelo TxGNN para el síndrome de inmunodeficiencia adquirida felina —causado por el Virus de Inmunodeficiencia Felina (FIV)— se fundamenta en la clasificación taxonómica compartida: tanto el VIH-1 como el FIV pertenecen al género *Lentivirus* de la familia Retroviridae. Sin embargo, esta analogía de clase presenta limitaciones estructurales críticas: la proteasa del FIV difiere del sitio activo de la proteasa del VIH-1 en residuos clave del bolsillo catalítico, lo que reduce considerablemente la probabilidad de inhibición cruzada eficaz por parte de los inhibidores de proteasa diseñados para el VIH humano. Los estudios de modelado molecular publicados indican que la mayoría de los inhibidores de proteasa del VIH exhiben actividad inhibitoria baja frente a la proteasa del FIV.

Como contexto relevante, la indicación de Rango 2 evaluada en este mismo reporte (infección por virus de inmunodeficiencia simiana, SIV) presenta una base mecanística notablemente más sólida: la proteasa del SIV comparte aproximadamente un 48–52% de identidad en la secuencia de aminoácidos con la proteasa del VIH-1, y cuatro estudios en primates no humanos demuestran que regímenes de terapia antirretroviral combinada que incluyen Darunavir logran supresión viral sostenida en modelos SIV. Esta indicación secundaria ofrece mayor potencial para exploración futura.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados con el uso de Darunavir en síndrome de inmunodeficiencia adquirida felina registrados.

> **⚠️ Nota sobre resultado recuperado:** El ensayo [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) fue indexado por la base de datos en asociación con esta indicación, pero corresponde a un estudio de Fase 4 en humanos infectados con VIH-1 (Darunavir potenciado + Lamivudina vs. triple terapia, n=145), completado en 2017. Su relevancia para la inmunodeficiencia felina (FIV) es **nula**; el resultado representa un error de etiquetado en la indexación de la base de datos, no evidencia real para esta indicación.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible sobre el uso de Darunavir en infección por FIV.

---

## Información de Mercado en Colombia

Darunavir no cuenta con registros sanitarios INVIMA activos en Colombia. La consulta a la base de datos regulatoria no arrojó ningún producto comercializado bajo este principio activo.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción del modelo TxGNN para el síndrome de inmunodeficiencia adquirida felina carece de sustento experimental directo. La proteasa del FIV presenta diferencias estructurales significativas respecto a la proteasa del VIH-1, y no existen estudios in vitro, preclínicos ni clínicos veterinarios que validen el uso de Darunavir en esta especie. El único ensayo clínico recuperado en la búsqueda es un estudio en humanos con VIH-1 mal etiquetado, lo que confirma la ausencia de evidencia real para esta indicación y sugiere sobreajuste del modelo en conexiones de red no específicas.

**Para avanzar se necesita:**
- Estudios in vitro de la actividad inhibitoria de Darunavir frente a la proteasa del FIV (ensayos enzimáticos y de replicación viral en líneas celulares felinas)
- Modelado por dinámica molecular comparativo entre las proteasas del VIH-1 y del FIV para cuantificar la afinidad de unión de Darunavir
- Verificación del mecanismo de acción (MOA) completo mediante consulta de DrugBank (pendiente, severidad Alta según el registro de brechas del Evidence Pack)
- Reorientar la estrategia de reposicionamiento hacia la indicación de Rango 2 (infección por SIV), que cuenta con evidencia animal (L3) y una base mecanística más sólida
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

